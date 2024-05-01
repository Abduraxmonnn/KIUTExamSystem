# Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Project
from apps.main.teachers.models import Teacher


class Subject(models.Model):
	full_name = models.CharField(max_length=255)
	stage = models.PositiveIntegerField()
	duration = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(180)])
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

	def __str__(self):
		return f'name: {self.full_name} | stage: {self.stage}'

	class Meta:
		verbose_name = 'Subject'
		verbose_name_plural = 'Subjects'
