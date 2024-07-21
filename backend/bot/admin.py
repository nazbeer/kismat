from django.contrib import admin
from .models import NudityMonitor

@admin.register(NudityMonitor)
class NudityMonitorAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

