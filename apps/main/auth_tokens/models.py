# Python
import binascii
import os

# Django
from django.db import models

# Project
from apps.main.exam_schedule.models import ExamSchedule


class CustomToken(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40, primary_key=True)
    schedule = models.OneToOneField(
        ExamSchedule, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name="Exam Schedule"
    )
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
        return self.schedule.student.full_name
