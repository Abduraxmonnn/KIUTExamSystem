# Rest-Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.main.answers.serializers import AnswerCreateSerializer
from apps.main.answers.services import create_answer_to_db_case_2
from apps.main.questions.models import Question
from apps.main.subjects.models import Subject
from apps.permissions import IsCustomTokenAuthenticatedPermission
from apps.services.get_user_by_token_service import get_student_by_token


class AnswerCreateAPIView(viewsets.ModelViewSet):
    model = Answer
    queryset = model.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [IsCustomTokenAuthenticatedPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        question_id = serializer.validated_data.get('question_id')
        subject_name = serializer.validated_data.get('subject_name')
        stage = serializer.validated_data.get('stage')
        picked = serializer.validated_data.get('picked', None)
        answer_json = serializer.validated_data.get('answer_json', None)
        file = serializer.validated_data.get('file', None)

        if stage == 2:
            response = create_answer_to_db_case_2(
                model=self.model,
                request=request,
                subject_name=subject_name,
                stage=stage,
                question_id=question_id,
                picked=picked
            )
            return response
