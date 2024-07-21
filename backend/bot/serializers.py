# bot/serializers.py
from rest_framework import serializers
from .models import NudityMonitor

class NudityMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NudityMonitor
        fields = ['user', 'start_time', 'end_time', 'detected']
