# discover/views.py
from rest_framework import generics
from .models import Discover, Nearby
from .serializers import DiscoverSerializer, NearbySerializer
from rest_framework.permissions import IsAuthenticated

class DiscoverListCreateView(generics.ListCreateAPIView):
    queryset = Discover.objects.all()
    serializer_class = DiscoverSerializer
    permission_classes = [IsAuthenticated]

class NearbyListCreateView(generics.ListCreateAPIView):
    queryset = Nearby.objects.all()
    serializer_class = NearbySerializer
    permission_classes = [IsAuthenticated]
