# party_room/serializers.py
from rest_framework import serializers
from .models import PartyRoom

class PartyRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyRoom
        fields = ['host', 'room_name', 'room_type', 'created_at']
