# RestFramework
from rest_framework import views, status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question
from apps.main.questions.serializers import QuestionRetrieveSerializer
from apps.main.questions.services import get_question_case_1_3, get_question_case_2
from apps.permissions import IsCustomTokenAuthenticatedPermission
from apps.services.get_user_by_token_service import get_student_by_token

groups_picker = {
    'U': 'UZ',
    'R': 'RU',
    'E': 'EN',
    'K': 'KR'
}


class QuestionRetrieveAPIView(views.APIView):
    model = Question
    serializer_class = QuestionRetrieveSerializer
    permission_classes = [IsCustomTokenAuthenticatedPermission]

    def post(self, request):
        student_group_letter = get_student_by_token(request).group.code[-1]

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')
        stage = serializer.validated_data.get('stage')
        number_of_questions = serializer.validated_data.get('number_of_questions')
        question_id = serializer.validated_data.get('question_id')

        try:
            get_questions = self.model.objects.get(
                subject__code=subject_code,
                stage=stage,
                language=groups_picker[student_group_letter]
            )
        #     ISSUE CATCHER
        except Question.MultipleObjectsReturned as ex:
            return Response({
                'status': 'error',
                'message': f'Check subject. That is not unique. exception: {ex}. query_params: {subject_code, stage, groups_picker[student_group_letter]}'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Question.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Check subject or stage and Try Again'
            }, status=status.HTTP_400_BAD_REQUEST)

        if stage == 1 or stage == 3:
            response = get_question_case_1_3(
                request=request,
                question_obj=get_questions,
                stage=stage,
                question_id=question_id,
                num_questions=number_of_questions
            )
            return response
        elif stage == 2:
            response = get_question_case_2(
                question_obj=get_questions,
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
