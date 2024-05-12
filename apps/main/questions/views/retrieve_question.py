# RestFramework
from rest_framework import views, status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question
from apps.main.questions.serializers import QuestionRetrieveSerializer
from apps.main.questions.services import get_question_case_1, get_question_case_2
from apps.permissions import IsCustomTokenAuthenticatedPermission
from apps.services.get_user_by_token_service import get_student_by_token


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
        question_id = serializer.validated_data.get('question_id')

        try:
            get_questions = self.model.objects.get(subject__full_name=subject, stage=stage)
        except Question.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Check subject or stage and Try Again'
            }, status=status.HTTP_400_BAD_REQUEST)

        if stage == 1:
            response = get_question_case_1(
                request=request,
                subject=subject,
                stage=stage,
                question_id=question_id,
                num_questions=number_of_questions
            )
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
            response = get_question_case_2(
                subject_name=subject,
                stage=stage,
                file_path=get_questions.file.name,
                question_id=question_id,
                num_questions=number_of_questions
            )
            return response
        else:
            return Response({
                'status': 'error',
                'message': 'Incorrect stage'
            }, status=status.HTTP_400_BAD_REQUEST)
