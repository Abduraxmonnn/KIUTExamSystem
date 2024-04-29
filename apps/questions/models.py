# Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Project
from apps.subjects.models import Subject


def upload_file_to(instance, filename):
    return f'questions/{instance.subject.full_name}/%Y/%m/{filename}'


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    stage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    file = models.FileField(upload_to=upload_file_to)

    def __str__(self):
        return f'{self.subject.full_name} {self.stage}'

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
