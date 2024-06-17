# Django
from django.db import models


class Direction(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Directions'
