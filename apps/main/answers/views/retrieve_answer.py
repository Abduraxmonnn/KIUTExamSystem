# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Project
from apps.main.answers.models import Answer
from apps.main.answers.serializers import RetrieveAnswerSerializer
from apps.permissions import IsTeacherTokenAuthenticatedPermission


class RetrieveAnswerAPIView(APIView):
    permission_classes = [IsTeacherTokenAuthenticatedPermission]

    def post(self, request):
        serializer = RetrieveAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        subject_code = serializer.validated_data.get('subject_code')
        student_rfid = serializer.validated_data.get('student_rfid')
        stage = serializer.validated_data.get('stage')

        if stage == 2:
            return Response({
                'status': 'error',
                'message': 'Score is not changeable for case 2'
            }, status=status.HTTP_400_BAD_REQUEST)

        get_answer = Answer.objects.get(subject__code=subject_code, student__rfid=student_rfid, stage=stage)

        data = {
            'student_rfid': get_answer.student.rfid,
            'subject': get_answer.subject.full_name,
            'score': get_answer.score,
            'answer_text': get_answer.answer_text
        }

        return Response({
            'status': 'successfully',
            'message': data
        }, status=status.HTTP_200_OK)
