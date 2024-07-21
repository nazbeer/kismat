# bot/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class NudityMonitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    detected = models.BooleanField(default=False)

    def __str__(self):
        return f"Nudity monitoring for {self.user.username}"
