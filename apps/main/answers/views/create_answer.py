# Rest-Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.main.answers.serializers import AnswerCreateSerializer
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
        subject = serializer.validated_data.get('subject')
        stage = serializer.validated_data.get('stage')
        answer_text = serializer.validated_data.get('answer_text', None)
        file = serializer.validated_data.get('file', None)

        try:
            get_student = get_student_by_token(request)
            get_question = Question.objects.get(pk=question_id)
            get_subject = Subject.objects.get(full_name=subject)
        except Exception as ex:
            print('---------> 33 line: create_answer: ', ex)
            return Response({
                'status': 'error',
                'message': 'Student / Question / Subject Does Not Exists!'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            created_answer = self.model.objects.create(
                subject=get_subject,
                stage=stage,
                question=get_question,
                student=get_student,
                answer_text=answer_text,
                file=file
            )
        except Exception as ex:
            print('Exception: ', ex)
            return Response({
                'status': 'error',
                'message': 'Raise Error while creating Answer. Please check input data one more time!'
            }, status=status.HTTP_400_BAD_REQUEST)

        created_answer.save()

        return Response({
            'status': 'successfully',
            'message': serializer.data
        }, status=status.HTTP_201_CREATED)
