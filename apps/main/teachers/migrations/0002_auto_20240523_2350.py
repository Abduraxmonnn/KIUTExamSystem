from django.db import migrations, models
import secrets
import string


def generate_random_password(password_length=6):
    characters = string.ascii_letters + string.digits + '!@#$%&'
    return ''.join(secrets.choice(characters) for _ in range(password_length))


def generate_random_username(username_length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(username_length))


def populate_login_password(apps, schema_editor):
    Teacher = apps.get_model('teachers', 'Teacher')
    existing_logins = set(Teacher.objects.values_list('login', flat=True))
    existing_passwords = set(Teacher.objects.values_list('password', flat=True))

    for teacher in Teacher.objects.all():
        # Ensure unique login
        login = generate_random_username()
        while login in existing_logins:
            login = generate_random_username()
        existing_logins.add(login)
        teacher.login = login

        # Ensure unique password
        password = generate_random_password()
        while password in existing_passwords:
            password = generate_random_password()
        existing_passwords.add(password)
        teacher.password = password

        teacher.save()


class Migration(migrations.Migration):
    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='login',
            field=models.CharField(max_length=6, default=generate_random_username),
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(max_length=6, default=generate_random_password),
        ),
        migrations.RunPython(populate_login_password),
    ]
