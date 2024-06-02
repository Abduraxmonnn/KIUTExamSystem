# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.main.students.models import Student
from apps.main.subjects.models import Subject
from apps.main.teachers_subjects.models import TeacherSubject
from apps.services.get_user_by_token_service import get_user_by_token

groups_picker = {
    'U': 'UZ',
    'R': 'RU',
    'E': 'EN',
    'K': 'KR'
}


def set_score_to_student(
        request,
        subject_code,
        student_id,
        score,
        stage
):
    if stage == 2:
        return Response({
            'status': 'error',
            'message': 'Score is not changeable for case 2'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        teacher_obj = get_user_by_token(request)
        answer_obj = Answer.objects.filter(subject__code=subject_code, student__student_id=student_id, stage=stage)
        student_group_obj = Student.objects.get(student_id=student_id)
        student_group_letter = student_group_obj.group.code[-1]
        print('--> ', answer_obj.last().subject)
        teacher_subject_obj = TeacherSubject.objects.get(teacher=teacher_obj, subject=answer_obj.last().subject,
                                                         language=groups_picker[student_group_letter])
    except Exception as ex:
        return Response({
            'status': 'error',
            'message': f'Raise error while getting Objects, {ex}'
        }, status=status.HTTP_400_BAD_REQUEST)

    if teacher_subject_obj.group.code != student_group_obj.group.code:
        return Response({
            'status': 'error',
            'message': 'Teacher Permission Denied'
        }, status=status.HTTP_403_FORBIDDEN)

    data = {
        'student_id': student_id,
        'score': None,
    }
    for item in answer_obj:
        item.score = score
        data['score'] = item.score
        item.save()

    return Response({
        'status': 'successfully',
        'message': data
    })
