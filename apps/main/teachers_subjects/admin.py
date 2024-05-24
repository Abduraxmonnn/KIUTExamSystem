# Django
from django.contrib import admin

# Project
from apps.main.teachers_subjects.models import TeacherSubject


@admin.register(TeacherSubject)
class TeacherSubjectAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'subject', 'language']
    list_display_links = ['teacher', 'subject']
    # search_fields = ['get_teacher']

    def get_teacher(self, obj):
        return obj.teacher.full_name
