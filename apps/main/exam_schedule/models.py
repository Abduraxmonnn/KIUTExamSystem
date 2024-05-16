from django.db import models

# Project
from apps.main.students.models import Student
from apps.main.subjects.models import Subject


class ExamSchedule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True, null=True)
    is_passed = models.BooleanField(default=False)
    room = models.PositiveIntegerField()
    exam_date = models.DateTimeField()
    is_paused = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    login = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f'{self.student.full_name} {self.subject.full_name} {self.is_passed}'

    class Meta:
        verbose_name = 'ExamSchedule'
        verbose_name_plural = 'ExamSchedules'
