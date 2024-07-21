# party_room/urls.py
from django.urls import path
from .views import PartyRoomListCreateView

urlpatterns = [
    path('', PartyRoomListCreateView.as_view(), name='party-room-list-create'),
]
