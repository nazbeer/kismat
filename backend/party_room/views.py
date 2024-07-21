# party_room/views.py
from rest_framework import generics
from .models import PartyRoom
from .serializers import PartyRoomSerializer
from rest_framework.permissions import IsAuthenticated

class PartyRoomListCreateView(generics.ListCreateAPIView):
    queryset = PartyRoom.objects.all()
    serializer_class = PartyRoomSerializer
    permission_classes = [IsAuthenticated]
