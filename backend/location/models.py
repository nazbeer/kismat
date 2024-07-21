from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point = models.PointField()

    def __str__(self):
        return f"Location of {self.user.username}"
