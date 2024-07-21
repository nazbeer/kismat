# gifts/views.py
from rest_framework import generics
from .models import Gift
from .serializers import GiftSerializer
from rest_framework.permissions import IsAuthenticated

class GiftListCreateView(generics.ListCreateAPIView):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = [IsAuthenticated]

class GiftDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = [IsAuthenticated]
