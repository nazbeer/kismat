# discover/urls.py
from django.urls import path
from .views import DiscoverListCreateView, NearbyListCreateView

urlpatterns = [
    path('discover/', DiscoverListCreateView.as_view(), name='discover-list-create'),
    path('nearby/', NearbyListCreateView.as_view(), name='nearby-list-create'),
]
