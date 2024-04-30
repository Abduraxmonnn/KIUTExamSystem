# Python
import binascii
import os

# RestFramework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.main.exam_schedule.models import ExamSchedule
from apps.main.exam_schedule.serializers import LogInSerializer
from apps.main.auth_tokens.models import CustomToken
from apps.permissions import LogInUserPermission


class LogInAPIView(APIView):
    model = ExamSchedule
    serializer_class = LogInSerializer
    permission_classes = [LogInUserPermission]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        login = serializer.validated_data.get('login')
        password = serializer.validated_data.get('password')

        schedule = ExamSchedule.objects.get(login=login, password=password)

        if not schedule:
            return Response({
                'status': 'error',
                'message': 'User does not Exists!'
            }, status=status.HTTP_401_UNAUTHORIZED)

        try:
            generate_token = CustomToken().generate_key()
            CustomToken.objects.create(key=generate_token, schedule=schedule)
        except Exception as ex:
            return Response({
                'status': 'error',
                'message': ex
            }, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'token': generate_token,
            'fullname': schedule.student.full_name,
            'subject': schedule.subject.full_name,
            'duration': schedule.subject.duration
        }

        return Response({
            'status': 'successfully',
            'message': dict(data),
        }, status=status.HTTP_200_OK)
