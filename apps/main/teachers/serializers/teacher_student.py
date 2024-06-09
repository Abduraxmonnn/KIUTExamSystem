# Rest-Framework
from rest_framework import serializers


class TeacherStudentsListSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=125)
    subject_lang = serializers.CharField(max_length=2)


class TeacherSetScoreSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=125)
    stage = serializers.IntegerField()
    student_id = serializers.CharField(max_length=20)
    score = serializers.IntegerField()


class TeacherWriteCommentSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=125)
    student_id = serializers.CharField(max_length=20)
    comment = serializers.CharField(max_length=1000, required=False)
