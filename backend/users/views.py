from rest_framework import generics, status
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a user by ID",
        responses={200: UserSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a user by ID",
        request_body=UserSerializer,
        responses={200: UserSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partially update a user by ID",
        request_body=UserSerializer,
        responses={200: UserSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class PasswordResetRequestView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Request a password reset",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
            },
            required=['email']
        ),
        responses={
            200: 'Password reset link sent.',
            400: 'User with this email does not exist.',
        }
    )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                url = reverse('password-reset-confirm', kwargs={'uidb64': uid, 'token': token})
                link = request.build_absolute_uri(url)
                send_mail(
                    'Password Reset Request',
                    f'Use this link to reset your password: {link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                )
                return Response({'message': 'Password reset link sent.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Confirm a password reset",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='New password'),
            },
            required=['password']
        ),
        responses={
            200: 'Password reset successful.',
            400: 'Invalid token or user.',
        }
    )
    def post(self, request, uidb64, token, *args, **kwargs):
        password = request.data.get('password')
        if password:
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
                if default_token_generator.check_token(user, token):
                    user.set_password(password)
                    user.save()
                    return Response({'message': 'Password reset successful.'}, status=status.HTTP_200_OK)
                return Response({'error': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'error': 'Invalid user.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Password is required.'}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Login a user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['username', 'password']
        ),
        responses={
            200: openapi.Response(
                description="Login successful with tokens.",
                examples={
                    "application/json": {
                        "refresh": "string",
                        "access": "string"
                    }
                }
            ),
            400: openapi.Response(
                description="Invalid credentials.",
                examples={
                    "application/json": {
                        "error": "Invalid credentials."
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

# Commented out GIS-related code as per your request to avoid GDAL and GEOS issues
# class UserLocationSearchView(generics.ListAPIView):
#     serializer_class = UserSerializer
#
#     def get_queryset(self):
#         queryset = User.objects.all()
#         location = self.request.query_params.get('location', None)
#         if location:
#             lat, lon = map(float, location.split(','))
#             user_location = Point(lon, lat, srid=4326)
#             queryset = queryset.annotate(distance=Distance('location', user_location)).order_by('distance')
#         return queryset
