from rest_framework import generics
from .models import VideoCall, Message
from .serializers import VideoCallSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated

class VideoCallListCreateView(generics.ListCreateAPIView):
    queryset = VideoCall.objects.all()
    serializer_class = VideoCallSerializer
    permission_classes = [IsAuthenticated]

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
