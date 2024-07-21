# chat/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', MessageListCreateView.as_view(), name='message-list-create'),
]
