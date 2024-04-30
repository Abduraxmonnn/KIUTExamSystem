# RestFramework
from rest_framework.views import APIView

# Project
from apps.main.exam_schedule.models import ExamSchedule
from apps.main.exam_schedule.serializers import LogInSerializer
from apps.permissions import LogInUserPermission
from apps.main.exam_schedule.services import login_data_checker


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

        return login_data_checker(schedule)
