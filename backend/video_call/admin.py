from django.contrib import admin
from .models import VideoCall

@admin.register(VideoCall)
class VideoCallAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

