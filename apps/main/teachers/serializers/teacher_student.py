# Rest-Framework
from rest_framework import serializers


class TeacherStudentsListSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=125)


class TeacherStudentsMaseScoreSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=20)
    student_rfid = serializers.CharField(max_length=30)
    score = serializers.IntegerField()
    stage = serializers.IntegerField()
