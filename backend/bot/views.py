# bot/views.py
from rest_framework import generics
from .models import NudityMonitor
from .serializers import NudityMonitorSerializer
from rest_framework.permissions import IsAuthenticated

class NudityMonitorListCreateView(generics.ListCreateAPIView):
    queryset = NudityMonitor.objects.all()
    serializer_class = NudityMonitorSerializer
    permission_classes = [IsAuthenticated]
