# RestFramework
from rest_framework import serializers

# Project
from apps.main.questions.models import Question


class QuestionRetrieveSerializer(serializers.ModelSerializer):
    number_of_questions = serializers.IntegerField(required=False, default=5)
    subject_code = serializers.CharField(max_length=125)
    question_id = serializers.CharField(max_length=25, required=False)
    testing = serializers.BooleanField(default=False)

    class Meta:
        model = Question
        fields = [
            'number_of_questions',
            'subject_code',
            'stage',
            'question_id',
            'testing'
        ]
