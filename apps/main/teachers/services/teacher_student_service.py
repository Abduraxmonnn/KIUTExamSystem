# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.services.get_user_by_token_service import get_user_by_token


def teacher_student_picker(request, subject_code):
    try:
        teacher_obj = get_user_by_token(request=request)
    except Exception as ex:
        return Response({
            'status': 'error',
            'message': f'Teacher Does Not Exists! {ex}'
        })

    student_groups = Answer.objects.filter(subject__code=subject_code)
    students_list = []
    unique_student_rfid = []
    case_1, case_2, case_3 = 0, 0, 0

    for item in student_groups:
        if item.stage == 1:
            case_1 = item.score
        elif item.stage == 2:
            case_2 = item.score
        else:
            case_3 = item.score

    for item in student_groups:
        tmp_res = {
            'student_rfid': item.student.rfid,
            'case_1_score': case_1,
            'case_2_score': case_2,
            'case_3_score': case_3
        }
        if item.student.rfid not in unique_student_rfid:
            students_list.append(tmp_res)
            unique_student_rfid.append(item.student.rfid)

    data = {
        'fullname': teacher_obj.full_name,
        'students': students_list
    }

    return Response({
        'status': 'successfully',
        'message': students_list
    }, status=status.HTTP_200_OK)
