# RestFramework
from rest_framework import serializers

# Project
from apps.main.questions.models import Question


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(max_length=255)

    class Meta:
        model = Question
        fields = [
            'subject',
            'stage',
        ]
