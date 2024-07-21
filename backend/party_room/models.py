# party_room/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PartyRoom(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255)
    room_type = models.CharField(max_length=50)  # Video or Voice
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name
