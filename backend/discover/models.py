# discover/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Discover(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Discover by {self.user.username}"

class Nearby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Nearby by {self.user.username}"
