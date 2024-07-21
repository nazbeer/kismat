# levels/serializers.py
from rest_framework import serializers
from .models import Level

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['user', 'balance', 'level']
