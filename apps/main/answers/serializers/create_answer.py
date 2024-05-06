# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.answers.models import Answer


class AnswerCreateSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField()
    subject = serializers.CharField(max_length=255)
    stage = serializers.IntegerField()

    class Meta:
        model = Answer
        fields = [
            'question_id',
            'subject',
            'stage',
            'answer_text',
            'file',
        ]
