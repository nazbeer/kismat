# gifts/models.py
from django.db import models

class Gift(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='gift_images/', blank=True)

    def __str__(self):
        return self.name
