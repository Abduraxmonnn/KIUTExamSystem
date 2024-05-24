# Rest-Framework
from rest_framework import serializers


class TeacherStudentsListSerializer(serializers.Serializer):
    subject_code = serializers.CharField(max_length=125)
