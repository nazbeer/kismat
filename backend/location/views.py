from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Location
from .serializers import LocationSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
