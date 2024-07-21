from django.contrib import admin
from .models import Discover, Nearby

@admin.register(Discover)
class DiscoverAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

@admin.register(Nearby)
class NearbyAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

