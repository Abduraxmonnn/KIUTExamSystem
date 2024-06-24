# Python
from datetime import datetime

# Django
from django.contrib import admin

# Project
from apps.main.exam_schedule.models import ExamSchedule


@admin.register(ExamSchedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    def time_seconds(self, obj):
        return obj.exam_date.strftime("%d %b %Y %H:%M:%S")

    time_seconds.admin_order_field = 'exam_date'
    time_seconds.short_description = 'Precise Time'

    list_display = ['id', 'subject', 'get_student_id', 'get_subject_code', 'exam_date', 'time_seconds', 'start_time']
    list_display_links = ['subject', 'get_student_id']
    search_fields = ['student__student_id', 'subject__full_name']

    def get_student_id(self, obj):
        return obj.student.student_id

    def get_subject_code(self, obj):
        return obj.subject.code
