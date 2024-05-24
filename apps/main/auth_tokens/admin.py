# Django
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Project
from apps.main.auth_tokens.models import CustomToken


@admin.register(CustomToken)
class CustomTokenAdmin(ModelAdmin):
    list_display = ['get_student_rfid', 'teacher', 'key']
    list_display_links = ['get_student_rfid', 'key']
    list_filter = ['is_student']
    # readonly_fields = ('key', )
    exclude = ('key', )

    def get_student_rfid(self, obj):
        if obj.schedule:
            return obj.schedule.student.rfid
