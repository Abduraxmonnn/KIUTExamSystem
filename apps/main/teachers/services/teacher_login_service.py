# Project
from rest_framework import status
from rest_framework.response import Response

from apps.main.auth_tokens.models import CustomToken
from apps.main.teachers_subjects.models import TeacherSubject


def teacher_login_data_checker(teacher_obj):
    get_subjects = TeacherSubject.objects.filter(teacher=teacher_obj)

    try:
        generate_token = CustomToken().generate_key()
        token, created = CustomToken.objects.get_or_create(teacher=teacher_obj, is_student=False)
        if created:
            token.key = generate_token
            token.save()

    except Exception as ex:
        return Response({
            'status': 'error',
            'message': ex
        }, status=status.HTTP_400_BAD_REQUEST)

    teacher_subject_code = []

    for item in get_subjects:
        tmp_res = {
            'name': item.subject.full_name,
            'code': item.subject.code
        }
        teacher_subject_code.append(tmp_res)

    data = {
        'token': generate_token if created else token.key,
        'fullname': teacher_obj.full_name,
        'subjects': teacher_subject_code
    }

    return Response({
        'status': 'successfully',
        'message': dict(data),
    }, status=status.HTTP_200_OK)
