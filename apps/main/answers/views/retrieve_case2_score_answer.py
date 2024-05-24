# Rest-Framework
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

# Project
from apps.main.answers.serializers import RetrieveCase2ScoreSerializer
from apps.main.answers.models import Answer
from apps.permissions import IsCustomTokenAuthenticatedPermission
from apps.services.get_user_by_token_service import get_user_by_token


class RetrieveCase2ScoreViewSet(ModelViewSet):
    model = Answer
    queryset = model.objects.select_related('subject', 'student', 'question')
    serializer_class = RetrieveCase2ScoreSerializer
    permission_classes = [IsCustomTokenAuthenticatedPermission]

    def get_object(self):
        subject_name = self.request.data['subject_name']
        try:
            get_student = get_user_by_token(self.request)
            queryset = self.filter_queryset(self.get_queryset())
            obj = queryset.filter(subject__full_name=subject_name, student=get_student).first()
        except Exception as ex:
            print('---------> 26 line: retrieve_case2_score_answer: ', ex)
            return Response({
                'status': 'error',
                'message': f'Answer Does Not Exists or Error! {ex}'
            }, status=status.HTTP_404_NOT_FOUND)
        return obj

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({
                'status': 'error',
                'message': f'Answer Does Not Exists or Error!'
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            'status': 'successfully',
            'message': {
                'subject': instance.subject.full_name,
                'student': instance.student.full_name,
                'student_id': instance.student.student_id,
                'student_group': instance.student.group.code,
                'score': instance.score,
            }
        }, status=status.HTTP_200_OK)
