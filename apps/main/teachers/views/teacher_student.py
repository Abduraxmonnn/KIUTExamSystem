# Rest-Framework
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.teachers.models import Teacher
from apps.main.teachers.serializers import TeacherStudentsListSerializer, TeacherStudentsMaseScoreSerializer
from apps.main.teachers.services import teacher_student_picker, teacher_make_score_to_student
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


class TeacherStudentsMaseScoreViewSet(ModelViewSet):
    model = Teacher
    queryset = model.objects.all()
    serializer_class = TeacherStudentsMaseScoreSerializer
    permission_classes = [IsCustomTokenAuthenticatedPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')
        student_rfid = serializer.validated_data.get('student_rfid')
        score = serializer.validated_data.get('score')
        stage = serializer.validated_data.get('stage')

        return teacher_make_score_to_student(
            request=request,
            subject_code=subject_code,
            student_rfid=student_rfid,
            score=score,
            stage=stage,
        )
