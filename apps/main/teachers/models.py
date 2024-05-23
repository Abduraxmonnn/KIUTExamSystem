# Python
import secrets

# Django
from django.db import models


def generate_random_password(password_length=6):
    """Generates a random number within the specified range (inclusive)."""
    return secrets.token_urlsafe(password_length)


# def generate_random_username(username_length=6):
#     """Generates a random number within the specified range (inclusive)."""
#     first_letter = names[0][0]
#     three_letters_surname = names[-1][:3]
#     number = '{:03d}'.format(random.randrange(1, 999))
#     username = (first_letter + three_letters_surname + number)
#     return username


class Teacher(models.Model):
    full_name = models.CharField(max_length=60)
    contact = models.CharField(max_length=30)
    login = models.CharField(max_length=6, unique=True, )
    password = models.CharField(max_length=6, unique=True, default=generate_random_password)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
