from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.geos import Point
from .models import Location
from .serializers import LocationSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        point = Point(self.request.data['longitude'], self.request.data['latitude'])
        serializer.save(user=self.request.user, point=point)
