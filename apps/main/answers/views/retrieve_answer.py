# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Project
from apps.main.answers.models import Answer
from apps.main.answers.serializers import RetrieveAnswerSerializer
from apps.main.answers.services import get_answer_from_db_to_case_1, get_answer_from_db_to_case_3
from apps.permissions import IsTeacherTokenAuthenticatedPermission


class RetrieveAnswerAPIView(APIView):
    permission_classes = [IsTeacherTokenAuthenticatedPermission]

    def post(self, request):
        serializer = RetrieveAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')
        student_id = serializer.validated_data.get('student_id')
        stage = serializer.validated_data.get('stage')

        if stage == 2:
            return Response({
                'status': 'error',
                'message': 'Score is not changeable for case 2'
            }, status=status.HTTP_400_BAD_REQUEST)

        get_answer = None
        if stage == 1:
            get_answer = get_answer_from_db_to_case_1(
                subject_code=subject_code,
                student_id=student_id,
                stage=stage
            )
        elif stage == 3:
            get_answer = get_answer_from_db_to_case_3(
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
