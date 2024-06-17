# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.services.get_deepest_element_serivce import get_deepest_element


def teacher_student_list(request, subject_code, subject_lang):
    student_scores = Answer.objects.filter(subject__code=subject_code, question__language=subject_lang)
    students_dict = {}

    try:
        for item in student_scores:
            student_id = item.student.student_id
            if student_id not in students_dict:
                students_dict[student_id] = {
                    'student_id': student_id,
                    'case_1_score': 0,
                    'case_3_score': 0
                }

            if item.stage == 1:
                students_dict[student_id]['case_1_score'] = get_deepest_element(item.score) if isinstance(
                    item.score, (
                        tuple, list)) else item.score
            elif item.stage == 3:
                students_dict[student_id]['case_3_score'] = get_deepest_element(item.score) if isinstance(
                    item.score, (
                        tuple, list)) else item.score

    except Exception as ex:
        return Response({
            'status': 'error',
            'message': f'raise error while collecting data. {ex}'
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        'status': 'successfully',
        'message': students_dict.values()
    }, status=status.HTTP_200_OK)
