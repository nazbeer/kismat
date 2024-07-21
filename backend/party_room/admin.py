from django.contrib import admin
from .models import PartyRoom

@admin.register(PartyRoom)
class PartyRoomAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

