# Django
from django.contrib import admin

# Project
from apps.main.auth_tokens.models import CustomToken


admin.site.register(CustomToken)
