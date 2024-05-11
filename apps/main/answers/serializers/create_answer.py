# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.answers.models import Answer


class AnswerCreateSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(max_length=255)
    stage = serializers.IntegerField()
    question_id = serializers.IntegerField()
    picked = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Answer
        fields = [
            'question_id',
            'subject_name',
            'stage',
            'picked',
            'answer_text',
        ]
