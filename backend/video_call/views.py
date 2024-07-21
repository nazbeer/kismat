# video_call/views.py
from rest_framework import generics
from .models import VideoCall
from .serializers import VideoCallSerializer
from rest_framework.permissions import IsAuthenticated

class VideoCallListCreateView(generics.ListCreateAPIView):
    queryset = VideoCall.objects.all()
    serializer_class = VideoCallSerializer
    permission_classes = [IsAuthenticated]
