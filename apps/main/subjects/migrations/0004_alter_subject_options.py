# Generated by Django 4.2 on 2024-05-22 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_alter_subject_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('full_name',), 'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
    ]
