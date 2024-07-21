from django.contrib import admin
from .models import Gift

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)

