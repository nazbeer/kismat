# bot/urls.py
from django.urls import path
from .views import NudityMonitorListCreateView

urlpatterns = [
    path('', NudityMonitorListCreateView.as_view(), name='nudity-monitor-list-create'),
]
