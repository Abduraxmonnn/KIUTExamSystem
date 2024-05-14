# Django
from django.db import models


class StudentGroup(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=128, blank=True, null=True, default='group')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.code

    class Meta:
        verbose_name = 'Student Group'
        verbose_name_plural = 'Student Groups'
