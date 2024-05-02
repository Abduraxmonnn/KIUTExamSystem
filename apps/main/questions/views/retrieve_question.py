# RestFramework
from rest_framework import views, status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question
from apps.main.questions.serializers import QuestionRetrieveSerializer
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

        try:
            get_questions = self.model.objects.get(subject__full_name=subject, stage=stage)
        except Question.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Check subject or stage and Try Again'
            }, status=status.HTTP_400_BAD_REQUEST)

        if stage != 2:
            response = dict({
                'file': get_questions.file.path
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
