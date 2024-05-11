# Rest-Framework
from rest_framework import viewsets

# Project
from apps.main.answers.models import Answer
from apps.main.answers.serializers import AnswerCreateSerializer
from apps.main.answers.services import create_answer_to_db_case_2
from apps.permissions import IsCustomTokenAuthenticatedPermission


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

        if stage == 1:
            response = ...
            return response
        elif stage == 2:
            response = create_answer_to_db_case_2(
                model=self.model,
                request=request,
                subject_name=subject_name,
                stage=stage,
                question_id=question_id,
                picked=picked
            )
            return response
