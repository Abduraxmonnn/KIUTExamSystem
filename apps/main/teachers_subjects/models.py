# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from apps.main.teachers.models import Teacher
from apps.main.subjects.models import Subject
from apps.main.student_groups.models import StudentGroup


class TeacherSubject(models.Model):
    class SubjectLang(models.TextChoices):
        UZBEK = 'UZ', _('Uzbek')
        RUSSIAN = 'RU', _('Russian')
        ENGLISH = 'EN', _('English')

    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    language = models.CharField(max_length=7, choices=SubjectLang.choices, default=SubjectLang.UZBEK)
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subject.full_name

    class Meta:
        verbose_name = 'Teacher Student'
        verbose_name_plural = 'Teachers Students'
