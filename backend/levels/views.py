# levels/views.py
from rest_framework import generics
from .models import Level
from .serializers import LevelSerializer
from rest_framework.permissions import IsAuthenticated

class LevelDetailView(generics.RetrieveUpdateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [IsAuthenticated]
