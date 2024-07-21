# discover/serializers.py
from rest_framework import serializers
from .models import Discover, Nearby

class DiscoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discover
        fields = ['user', 'content']

class NearbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nearby
        fields = ['user', 'location']
