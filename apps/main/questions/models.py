# Python
from datetime import datetime

# Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from apps.main.subjects.models import Subject


def upload_file_to(instance, filename):
    return f'questions/{instance.subject.code}/{filename}'


class Question(models.Model):

    class ExamLang(models.TextChoices):
        UZBEK = 'UZ', _('Uzbek')
        RUSSIAN = 'RU', _('Russian')
        ENGLISH = 'EN', _('English')
        KOREAN = 'KR', _('Korean')

    specialization = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    language = models.CharField(max_length=7, choices=ExamLang.choices, default=ExamLang.UZBEK)
    academic_semester = models.PositiveIntegerField(default=0)
    stage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    file = models.FileField(upload_to=upload_file_to)

    def __str__(self):
        return self.specialization

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
