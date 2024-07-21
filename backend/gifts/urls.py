# gifts/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', GiftListCreateView.as_view(), name='gift-list-create'),
    path('<int:pk>/', GiftDetailView.as_view(), name='gift-detail'),
]
