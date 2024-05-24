# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer


def teacher_make_score_to_student(
        request,
        subject_code,
        student_rfid,
        score,
        stage
):
    if stage == 2:
        return Response({
            'status': 'error',
            'message': 'Score is not changeable for case 2'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        answer_obj = Answer.objects.get(
            subject__code=subject_code,
            student__rfid=student_rfid,
            stage=stage
        )
        answer_obj.score = score
        answer_obj.save()
    except Exception as ex:
        return Response({
            'status': 'error',
            'message': f'Answer Does Not Exists! {ex}'
        })

    return Response({
        'status': 'successfully',
        'message': 'Score updated!'
    }, status=status.HTTP_200_OK)
