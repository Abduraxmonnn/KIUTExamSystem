# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.main.answers.services.get_answer_case_2 import generate_and_save_docx_case_2
# Project
from apps.services.get_user_by_token_service import get_user_by_token
from apps.main.answers.serializers import RetrieveAnswerSerializer
from apps.main.answers.services import get_answer_from_db_to_case_1, \
    get_answer_from_db_to_case_3
from apps.permissions import IsTeacherTokenAuthenticatedPermission


class RetrieveAnswerAPIView(APIView):
    permission_classes = [IsTeacherTokenAuthenticatedPermission]

    def post(self, request):
        serializer = RetrieveAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')
        student_id = serializer.validated_data.get('student_id')
        stage = serializer.validated_data.get('stage')

        get_user = get_user_by_token(request)

        teacher_split_name = get_user.full_name.split(None)
        target_name = ['ALLAKULIEV', 'AKMAL']

        get_answer = None
        if stage == 2:
            if target_name[0] not in teacher_split_name or target_name[1] not in teacher_split_name:
                return Response({
                    'status': 'error',
                    'message': 'Score is not changeable for case 2'
                }, status=status.HTTP_400_BAD_REQUEST)

            get_answer = generate_and_save_docx_case_2(student_id=student_id, subject_code=subject_code)

        if stage == 1:
            get_answer = get_answer_from_db_to_case_1(
                subject_code=subject_code,
                student_id=student_id,
                stage=stage
            )
        elif stage == 3:
            get_answer = get_answer_from_db_to_case_3(
                request=request,
                subject_code=subject_code,
                student_id=student_id,
                stage=stage
            )

        if 'error' in get_answer['status']:
            return Response({
                'status': 'error',
                'message': get_answer['message']
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status': 'successfully',
            'message': get_answer['message']
        }, status=status.HTTP_200_OK)
