# wallet/views.py
from rest_framework import generics
from .models import Wallet
from .serializers import WalletSerializer
from rest_framework.permissions import IsAuthenticated

class WalletDetailView(generics.RetrieveUpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]
