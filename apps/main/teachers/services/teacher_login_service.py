# Project
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.auth_tokens.models import CustomToken
from apps.main.questions.models import Question
from apps.main.teachers_subjects.models import TeacherSubject


def get_subject_codes(subjects):
    teacher_subject_code = []
    for item in subjects:
        tmp_res = {
            'name': item.subject.full_name,
            'code': item.subject.code
        }
        teacher_subject_code.append(tmp_res)
    return teacher_subject_code


def teacher_login_data_checker(teacher_obj):
    get_subjects = TeacherSubject.objects.filter(teacher=teacher_obj)

    try:
        token = CustomToken.objects.get(teacher=teacher_obj, is_student=False)

    except CustomToken.DoesNotExist:
        generate_token = CustomToken().generate_key()
        token = CustomToken.objects.create(teacher=teacher_obj, is_student=False, key=generate_token)

    unique_subjects = get_subjects.distinct('subject__id')
    teacher_subject_code = [
        {
            'name': item.subject.full_name,
            'code': item.subject.code,
            'language': set(i.language for i in get_subjects),
            'subject_stages': set(
                Question.objects.filter(subject=item.subject, subject__code=item.subject.code).values_list('stage',
                                                                                                           flat=True))
        }
        for item in unique_subjects
    ]

    data = {
        'token': token.key,
        'fullname': teacher_obj.full_name,
        'subjects': teacher_subject_code
    }

    return Response({
        'status': 'successfully',
        'message': dict(data),
    }, status=status.HTTP_200_OK)
