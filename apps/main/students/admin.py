# Django
from django.contrib import admin

# Project
from apps.main.students.models import Student


admin.site.register(Student)
