# Rest-Framework
from rest_framework import serializers


class TeacherLogInSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=12)
    password = serializers.CharField(max_length=12)
