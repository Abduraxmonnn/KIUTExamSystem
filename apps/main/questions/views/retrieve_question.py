# RestFramework
from rest_framework import views, status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question
from apps.main.questions.serializers import QuestionRetrieveSerializer
from apps.main.questions.services import get_question_case_1
from apps.permissions import IsCustomTokenAuthenticatedPermission


class QuestionRetrieveAPIView(views.APIView):
    model = Question
    serializer_class = QuestionRetrieveSerializer
    permission_classes = [IsCustomTokenAuthenticatedPermission]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject = serializer.validated_data.get('subject')
        stage = serializer.validated_data.get('stage')
        number_of_questions = serializer.validated_data.get('number_of_questions')

        try:
            get_questions = self.model.objects.get(subject__full_name=subject, stage=stage)
        except Question.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Check subject or stage and Try Again'
            }, status=status.HTTP_400_BAD_REQUEST)

        if stage == 1:
            response = get_question_case_1(subject=subject, stage=stage, num_questions=number_of_questions)
            return response
        if stage == 3:
            response = dict({
                'specialization': get_questions.specialization,
                'language': get_questions.language,
                'academic_semester': get_questions.academic_semester,
                'file': get_questions.file.url
            })

            return Response({
                'status': 'successfully',
                'message': response
            }, status=status.HTTP_200_OK)
        elif stage == 2:
            ...
        else:
            return Response({
                'status': 'error',
                'message': 'Incorrect stage'
            }, status=status.HTTP_400_BAD_REQUEST)
