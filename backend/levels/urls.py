# levels/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', LevelDetailView.as_view(), name='level-detail'),
]
