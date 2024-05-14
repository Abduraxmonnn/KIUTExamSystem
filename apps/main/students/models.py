# Django
from django.db import models

# Project
from apps.main.directions.models import Direction
from apps.main.student_groups.models import StudentGroup


class Student(models.Model):
    full_name = models.CharField(max_length=60)
    student_id = models.CharField(max_length=20)
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True)
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)
    rfid = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
