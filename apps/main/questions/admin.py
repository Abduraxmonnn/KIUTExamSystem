# Django
from django.contrib import admin

# Project
from apps.main.questions.models import Question


admin.site.register(Question)
