# video_call/serializers.py
from rest_framework import serializers
from .models import VideoCall

class VideoCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCall
        fields = ['caller', 'receiver', 'start_time', 'end_time', 'status']
