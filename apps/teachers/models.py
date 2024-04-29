# Django
from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=60)
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
