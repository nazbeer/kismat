# wallet/urls.py
from django.urls import path
from .views import WalletDetailView

urlpatterns = [
    path('<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),
]
