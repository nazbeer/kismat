from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class VideoCall(models.Model):
    caller = models.ForeignKey(User, related_name='video_call_as_caller', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='video_call_as_receiver', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.caller.username} to {self.receiver.username}"

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)
    video_call = models.ForeignKey(VideoCall, related_name='messages', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"
