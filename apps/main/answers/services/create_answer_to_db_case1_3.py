# Python
import requests

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.main.questions.models import Question
from apps.main.subjects.models import Subject
from apps.services.get_user_by_token_service import get_student_by_token


def create_answer_case_1_3(stage: int,
                           request: requests,
                           subject_name: str,
                           question_id: int,
                           answer_text: str) -> Response:
    """
    :param stage: stage (case) of answer
    :param request:
    :param subject_name: subject name which one student applied
    :param question_id: question ID which question answered
    :param answer_text: student's answer to a question
    :return Response:
    """
    groups_picker = {
        'U': 'UZ',
        'R': 'RU',
        'E': 'EN',
        'K': 'KR'
    }

    try:
        get_student = get_student_by_token(request)
        student_group_letter = get_student.group.code[-1]
        get_question = Question.objects.get(
            subject__full_name=subject_name,
            stage=stage,
            language=groups_picker[student_group_letter])
        get_subject = Subject.objects.get(full_name=subject_name)
    except Exception as ex:
        print('---------> 27 line: create_answer_case1_service: ', ex)
        return Response({
            'status': 'error',
            'message': f'Student / Question / Subject Does Not Exists or Error! {ex}'
        }, status=status.HTTP_400_BAD_REQUEST)

    response = {
        'subject_name': subject_name,
        'question_id': question_id,
        'student': get_student.full_name,
        'answer_text': answer_text
    }

    try:
        Answer.objects.create(
            subject=get_subject,
            stage=stage,
            student=get_student,
            question=get_question,
            question_ids=question_id,
            answer_text=answer_text
        ).save()
    except Exception as ex:
        print('---------> 50 line: create_answer_case1_service: ', ex)
        return Response({
            'status': 'error',
            'message': f'Raise error while creating Answer object! {ex}'
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        'status': 'successfully',
        'message': response
    }, status=status.HTTP_201_CREATED)
