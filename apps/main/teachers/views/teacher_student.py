# Rest-Framework
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.teachers.models import Teacher
from apps.main.teachers.serializers import TeacherStudentsListSerializer, TeacherSetScoreSerializer, \
    TeacherWriteCommentSerializer
from apps.main.teachers.services import teacher_student_list, set_score_to_student, write_comment_to_student, \
    get_comment_from_db
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
        subject_lang = serializer.validated_data.get('subject_lang')

        return teacher_student_list(request=request, subject_code=subject_code, subject_lang=subject_lang)


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
        comment = serializer.validated_data.get('comment', None)

        return set_score_to_student(
            request=request,
            subject_code=subject_code,
            student_id=student_id,
            score=score,
            comment=comment,
            stage=stage
        )


class TeacherWriteCommentViewSet(ModelViewSet):
    model = Teacher
    queryset = model.objects.all()
    serializer_class = TeacherWriteCommentSerializer
    permission_classes = [IsTeacherTokenAuthenticatedPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')
        student_id = serializer.validated_data.get('student_id')
        comment = serializer.validated_data.get('comment')

        return write_comment_to_student(
            request=request,
            subject_code=subject_code,
            student_id=student_id,
            comment=comment,
        )


class TeacherRetrieveCommentViewSet(ModelViewSet):
    model = Teacher
    queryset = model.objects.all()
    serializer_class = TeacherWriteCommentSerializer
    permission_classes = [IsTeacherTokenAuthenticatedPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')
        student_id = serializer.validated_data.get('student_id')

        return get_comment_from_db(
            request=request,
            subject_code=subject_code,
            student_id=student_id,
        )
