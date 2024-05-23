# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.answers.models import Answer


class RetrieveCase2ScoreSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(max_length=255)
    subject_code = serializers.CharField(max_length=125)

    class Meta:
        model = Answer
        fields = [
            'subject_name'
        ]
