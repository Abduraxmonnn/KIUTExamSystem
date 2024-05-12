# Python
from datetime import datetime

# RestFramework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.auth_tokens.models import CustomToken
from apps.main.questions.models import Question


def login_data_checker(schedule):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exam_date_obj = schedule.exam_date.strftime("%Y-%m-%d %H:%M:%S")

    if not schedule:
        return Response({
            'status': 'error',
            'message': 'User does not Exists!'
        }, status=status.HTTP_401_UNAUTHORIZED)
    elif exam_date_obj < current_time:
        return Response({
            'status': 'error',
            'message': 'Exam Time is Expired'
        }, status=status.HTTP_401_UNAUTHORIZED)

    try:
        generate_token = CustomToken().generate_key()
        token, created = CustomToken.objects.get_or_create(schedule=schedule)
        if created:
            token.key = generate_token
            token.save()
    except Exception as ex:
        return Response({
            'status': 'error',
            'message': ex
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        if schedule.start_time is None:
            schedule.start_time = current_time
            schedule.save()
    except Exception as ex:
        return Response({
            'status': 'error',
            'message': ex
        }, status=status.HTTP_400_BAD_REQUEST)

    q = Question.objects.filter(subject=schedule.subject)
    print(q)

    data = {
        'token': generate_token if created else token.key,
        'fullname': schedule.student.full_name,
        'subject': schedule.subject.full_name,
        # 'subject_stage': q,
        'duration': schedule.subject.duration
    }

    return Response({
        'status': 'successfully',
        'message': dict(data),
    }, status=status.HTTP_200_OK)
