# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.answers.models import Answer


class RetrieveCase2ScoreSerializer(serializers.ModelSerializer):
    subject_code = serializers.CharField(max_length=125)

    class Meta:
        model = Answer
        fields = [
            'subject_code'
        ]


class RetrieveAnswerSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=125)
    student_rfid = serializers.CharField(max_length=30)
    stage = serializers.IntegerField()
