# Django
from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=60)
    student_id = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
