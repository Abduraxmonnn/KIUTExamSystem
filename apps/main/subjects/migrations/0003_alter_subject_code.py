# Generated by Django 4.2 on 2024-05-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_remove_subject_teacher_subject_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
