from django.contrib import admin
from .models import VideoCall, Message

@admin.register(VideoCall)
class VideoCallAdmin(admin.ModelAdmin):
    list_display = ('caller', 'receiver', 'start_time', 'end_time')
    search_fields = ('caller__username', 'receiver__username')
    list_filter = ('start_time', 'end_time')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'video_call', 'message', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'message')
    list_filter = ('timestamp',)
