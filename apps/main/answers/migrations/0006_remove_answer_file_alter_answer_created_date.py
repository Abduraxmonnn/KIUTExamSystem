# Generated by Django 4.2 on 2024-05-11 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0005_answer_answer_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='file',
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
