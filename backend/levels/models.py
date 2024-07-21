# levels/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Level(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - Level {self.level}"
