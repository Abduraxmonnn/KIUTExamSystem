# Rest-Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.main.answers.serializers import AnswerCreateSerializer
from apps.main.answers.services import create_answer_to_db_case_2, create_answer_case_1_3
from apps.main.questions.models import Question
from apps.main.subjects.models import Subject
from apps.permissions import IsCustomTokenAuthenticatedPermission
from apps.services.get_user_by_token_service import get_user_by_token

groups_picker = {
    'U': 'UZ',
    'R': 'RU',
    'E': 'EN',
    'K': 'KR'
}


class AnswerCreateAPIView(viewsets.ModelViewSet):
    model = Answer
    queryset = model.objects.all()
    serializer_class = AnswerCreateSerializer
    permission_classes = [IsCustomTokenAuthenticatedPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        question_id = serializer.validated_data.get('question_id')
        subject_code = serializer.validated_data.get('subject_code')
        stage = serializer.validated_data.get('stage')
        picked = serializer.validated_data.get('picked', None)
        answer_text = serializer.validated_data.get('answer_text', None)

        try:
            get_student = get_user_by_token(request)
            student_group_letter = get_student.group.code[-1]
            get_question = Question.objects.get(
                subject__code=subject_code,
                stage=stage,
                language=groups_picker[student_group_letter])
            get_subject = Subject.objects.get(code=subject_code)
        except Exception as ex:
            print('---------> 49 line: create_answer_api: ', ex)
            return Response({
                'status': 'error',
                'message': f'Student / Question / Subject Does Not Exists or Error! {ex}'
            }, status=status.HTTP_400_BAD_REQUEST)

        if stage == 1 or stage == 3:
            response = create_answer_case_1_3(
                stage=stage,
                request=request,
                question_obj=get_question,
                subject_obj=get_subject,
                student_obj=get_student,
                question_id=question_id,
                answer_text=answer_text
            )
            return response
        elif stage == 2:
            response = create_answer_to_db_case_2(
                model=self.model,
                request=request,
                student_obj=get_student,
                subject_obj=get_subject,
                stage=stage,
                question_obj=get_question,
                question_id=question_id,
                picked=picked
            )
            return response
        else:
            return Response({
                'status': 'error',
                'message': f'Please Check Input Data!'
            }, status=status.HTTP_400_BAD_REQUEST)
