# gifts/serializers.py
from rest_framework import serializers
from .models import Gift

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['id', 'name', 'description', 'price', 'image']
