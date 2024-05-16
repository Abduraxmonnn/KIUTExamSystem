# Django
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Project
from apps.main.auth_tokens.models import CustomToken


@admin.register(CustomToken)
class CustomTokenAdmin(ModelAdmin):
    list_display = ['schedule', 'key']
    list_display_links = ['schedule', 'key']
    # readonly_fields = ('key', )
    exclude = ('key', )
