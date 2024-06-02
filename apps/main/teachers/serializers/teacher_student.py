# Rest-Framework
from rest_framework import serializers


class TeacherStudentsListSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=125)


class TeacherSetScoreSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=125)
    stage = serializers.IntegerField()
    student_id = serializers.CharField(max_length=20)
    score = serializers.IntegerField()
