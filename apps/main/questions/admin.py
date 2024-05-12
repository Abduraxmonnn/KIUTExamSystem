# Django
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Project
from apps.main.questions.models import Question


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ['id', 'subject', 'stage', 'language', 'get_file_name']
    list_display_links = ['subject', 'language']
    list_filter = ['stage', 'language']

    def get_file_name(self, obj):
        file = obj.file.name
        file_name = file.split('/' or '\\')[-1]
        return file_name
