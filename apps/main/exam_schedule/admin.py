# Django
from django.contrib import admin

# Project
from apps.main.exam_schedule.models import ExamSchedule


admin.site.register(ExamSchedule)
