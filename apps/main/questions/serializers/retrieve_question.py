# RestFramework
from rest_framework import serializers

# Project
from apps.main.questions.models import Question


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    number_of_questions = serializers.IntegerField(required=False, default=5)
    subject = serializers.CharField(max_length=255)

    class Meta:
        model = Question
        fields = [
            'number_of_questions',
            'subject',
            'stage',
        ]
