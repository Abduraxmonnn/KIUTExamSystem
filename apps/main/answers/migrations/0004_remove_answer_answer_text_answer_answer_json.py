# Generated by Django 4.2 on 2024-05-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0003_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_text',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_json',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
