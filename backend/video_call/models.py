# video_call/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class VideoCall(models.Model):
    caller = models.ForeignKey(User, related_name='caller', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20)  # Ongoing, Ended

    def __str__(self):
        return f"Call from {self.caller.username} to {self.receiver.username}"
