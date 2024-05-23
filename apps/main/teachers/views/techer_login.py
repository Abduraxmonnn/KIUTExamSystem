# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Project
from apps.main.teachers.models import Teacher
from apps.main.teachers.serializers import TeacherLogInSerializer


class TeacherLogInAPIView(APIView):

    def post(self, request):
        serializer = TeacherLogInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        login = serializer.validated_data.get('login')
        password = serializer.validated_data.get('password')

