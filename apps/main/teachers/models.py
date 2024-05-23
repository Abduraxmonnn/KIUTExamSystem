import secrets
import string
import random

# Django
from django.db import models


def generate_random_password(password_length=6):
    """Generates a random password with the specified length."""
    characters = string.ascii_letters + string.digits + '!@#$%&'
    return ''.join(secrets.choice(characters) for _ in range(password_length))


def generate_random_username(username_length=6):
    """Generates a random username with the specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(username_length))


class Teacher(models.Model):
    full_name = models.CharField(max_length=60)
    contact = models.CharField(max_length=30)
    login = models.CharField(max_length=6, unique=True, default=generate_random_username)
    password = models.CharField(max_length=6, unique=True, default=generate_random_password)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
