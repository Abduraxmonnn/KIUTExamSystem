# Django
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Project
from apps.main.teachers.models import Teacher
from apps.main.directions.models import Direction


class Subject(models.Model):
	code = models.CharField(max_length=20, unique=True)
	full_name = models.CharField(max_length=255)
	stage = models.PositiveIntegerField()
	duration = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(180)])
	direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.full_name

	class Meta:
		verbose_name = 'Subject'
		verbose_name_plural = 'Subjects'
