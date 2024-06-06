# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.main.teachers_subjects.models import TeacherSubject
from apps.services.get_user_by_token_service import get_user_by_token


def get_deepest_element(data):
    if isinstance(data, (tuple, list)):
        for item in data:
            result = get_deepest_element(item)
            if result is not None:
                return result
    else:
        return data
    return None


def teacher_student_picker(request, subject_code):
    try:
        get_teacher = get_user_by_token(request)
        teacher_subject_obj = TeacherSubject.objects.filter(teacher=get_teacher)
        teacher_subject_lang_list = set(i.language for i in teacher_subject_obj)
    except Exception as ex:
        return Response({
            'status': 'error',
            'message': f'Teacher Does not Exists. {ex}'
        }, status=status.HTTP_400_BAD_REQUEST)

    students_list = []
    for item in teacher_subject_lang_list:
        student_scores = Answer.objects.filter(subject__code=subject_code, question__language=item)
        students_dict = {}

        try:
            for item in student_scores:
                student_id = item.student.student_id
                if student_id not in students_dict:
                    students_dict[student_id] = {
                        'student_id': student_id,
                        'case_1_score': 0,
                        #        'case_2_score': 0,
                        'case_3_score': 0
                    }

                if item.stage == 1:
                    students_dict[student_id]['case_1_score'] = get_deepest_element(item.score) if isinstance(
                        item.score, (
                            tuple, list)) else item.score
                # elif item.stage == 2:
                #     students_dict[student_id]['case_2_score'] = get_deepest_element(item.score) if isinstance(item.score, (
                #         tuple, list)) else item.score
                elif item.stage == 3:
                    students_dict[student_id]['case_3_score'] = get_deepest_element(item.score) if isinstance(
                        item.score, (
                            tuple, list)) else item.score

            students_list.append(students_dict.values())
        except Exception as ex:
            return Response({
                'status': 'error',
                'message': f'raise error while collecting data. {ex}'
            }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        'status': 'successfully',
        'message': students_list
    }, status=status.HTTP_200_OK)
