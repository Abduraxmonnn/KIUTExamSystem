# Python
from datetime import datetime, timedelta

# RestFramework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.auth_tokens.models import CustomToken
from apps.main.questions.models import Question


def student_login_data_checker(schedule):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exam_date_obj = schedule.exam_date.strftime("%Y-%m-%d %H:%M:%S")

    if not schedule:
        return Response({
            'status': 'error',
            'message': 'User does not Exists!'
        }, status=status.HTTP_401_UNAUTHORIZED)
    # elif exam_date_obj < current_time:
    #     return Response({
    #         'status': 'error',
    #         'message': 'Exam Time is Expired'
    #     }, status=status.HTTP_401_UNAUTHORIZED)

    if schedule.start_time:
        return Response({
            'status': 'error',
            'message': 'User can Login Once'
        }, status=status.HTTP_401_UNAUTHORIZED)

    try:
        question_stages = set(Question.objects.filter(subject=schedule.subject, subject__code=schedule.subject.code).values_list('stage', flat=True))

    except Exception as ex:
        return Response({
            'status': 'error',
            'message': ex
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        existing_token = CustomToken.objects.filter(schedule=schedule).first()

        if existing_token:
            token = existing_token
        else:
            token = CustomToken(schedule=schedule, is_student=True)
            token.save()

        if schedule.start_time is None:
            schedule.start_time = current_time
            schedule.save()
    except Exception as ex:
        return Response({
            'status': 'error',
            'message': ex
        }, status=status.HTTP_400_BAD_REQUEST)

    data = {
        'token': token.key,
        'fullname': schedule.student.full_name,
        'subject': schedule.subject.full_name,
        'subject_code': schedule.subject.code,
        'subject_stage': question_stages,
        'duration': schedule.subject.duration
    }

    return Response({
        'status': 'successfully',
        'message': dict(data),
    }, status=status.HTTP_200_OK)
