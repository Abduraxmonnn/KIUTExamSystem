# Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Project
from apps.subjects.models import Subject
from apps.students.models import Student


def upload_file_to(instance, filename):
    return f'answers/{instance.subject.full_name}/%Y/%m/{filename}'


class Answer(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    stage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to=upload_file_to)

    def __str__(self):
        return f'{self.subject.full_name} {self.stage} {self.student.full_name}'

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
