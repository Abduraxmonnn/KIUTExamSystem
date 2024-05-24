# Python
import binascii
import os

# Django
from django.db import models

# Project
from apps.main.exam_schedule.models import ExamSchedule
from apps.main.teachers.models import Teacher


class CustomToken(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40, primary_key=True)
    schedule = models.OneToOneField(
        ExamSchedule, related_name='schedule_auth_token',
        on_delete=models.CASCADE, verbose_name="Exam Schedule",
        blank=True, null=True
    )
    teacher = models.OneToOneField(
        Teacher, related_name='teacher_auth_token',
        on_delete=models.CASCADE, verbose_name="Teacher",
        blank=True, null=True
    )
    is_student = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(CustomToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        if self.schedule:
            return self.schedule.student.full_name
        else:
            return self.teacher.full_name
