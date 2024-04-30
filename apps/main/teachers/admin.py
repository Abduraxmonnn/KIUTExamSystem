# Django
from django.contrib import admin

# Project
from apps.main.teachers.models import Teacher


admin.site.register(Teacher)
