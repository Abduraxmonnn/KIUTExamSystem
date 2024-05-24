# Rest-Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Project
from apps.main.teachers.models import Teacher
from apps.main.teachers.serializers import TeacherLogInSerializer
from apps.main.teachers.services import teacher_login_data_checker
from apps.permissions import LogInUserPermission


class TeacherLogInAPIView(APIView):
    model = Teacher
    serializer_class = TeacherLogInSerializer
    permission_classes = [LogInUserPermission]

    def post(self, request):
        serializer = TeacherLogInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        login = serializer.validated_data.get('login')
        password = serializer.validated_data.get('password')

        try:
            teacher_obj = Teacher.objects.get(login=login, password=password)
        except Teacher.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'User does not Exists!'
            }, status=status.HTTP_401_UNAUTHORIZED)

        return teacher_login_data_checker(teacher_obj=teacher_obj)
