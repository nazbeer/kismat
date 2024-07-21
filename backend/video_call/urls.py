# video_call/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', VideoCallListCreateView.as_view(), name='video-call-list-create'),
]
