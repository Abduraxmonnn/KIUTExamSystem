# Python
from datetime import datetime

# Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Project
from apps.main.subjects.models import Subject
from apps.main.students.models import Student
from apps.main.questions.models import Question


def upload_file_to(instance, filename):
    return f'answers/{instance.subject.code}/{filename}'


class Answer(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    stage = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    question_ids = models.CharField(max_length=155, blank=True, null=True)
    score = models.PositiveIntegerField(default=0)
    is_scored = models.BooleanField(default=False)
    answer_json = models.JSONField(blank=True, null=True)
    answer_text = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject.full_name} {self.stage} {self.student.full_name}'

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
