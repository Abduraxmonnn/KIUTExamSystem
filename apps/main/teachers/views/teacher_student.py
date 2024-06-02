# Rest-Framework
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.teachers.models import Teacher
from apps.main.teachers.serializers import TeacherStudentsListSerializer, TeacherSetScoreSerializer
from apps.main.teachers.services import teacher_student_picker, set_score_to_student
from apps.permissions import IsTeacherTokenAuthenticatedPermission


class TeacherStudentsListViewSet(ModelViewSet):
    model = Teacher
    queryset = model.objects.all()
    serializer_class = TeacherStudentsListSerializer
    permission_classes = [IsTeacherTokenAuthenticatedPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')

        return teacher_student_picker(subject_code=subject_code)


class TeacherSetScoreViewSet(ModelViewSet):
    model = Teacher
    queryset = model.objects.all()
    serializer_class = TeacherSetScoreSerializer
    permission_classes = [IsTeacherTokenAuthenticatedPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')
        student_id = serializer.validated_data.get('student_id')
        score = serializer.validated_data.get('score')
        stage = serializer.validated_data.get('stage')

        return set_score_to_student(
            request=request,
            subject_code=subject_code,
            student_id=student_id,
            score=score,
            stage=stage
        )
