# Rest-Framework
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.teachers.models import Teacher
from apps.main.teachers.serializers import TeacherStudentsListSerializer
from apps.main.teachers.services import teacher_student_picker
from apps.permissions import IsCustomTokenAuthenticatedPermission


class TeacherStudentsListViewSet(ModelViewSet):
    model = Teacher
    queryset = model.objects.all()
    serializer_class = TeacherStudentsListSerializer
    permission_classes = [IsCustomTokenAuthenticatedPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')

        return teacher_student_picker(request=request, subject_code=subject_code)
