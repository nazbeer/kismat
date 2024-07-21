from rest_framework import serializers
from .models import VideoCall, Message

class VideoCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCall
        fields = ['id', 'caller', 'receiver', 'start_time', 'end_time']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'video_call', 'message', 'timestamp']
