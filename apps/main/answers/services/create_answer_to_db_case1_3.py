# Python
import requests

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.main.questions.models import Question
from apps.main.subjects.models import Subject
from apps.services.get_user_by_token_service import get_user_by_token


def create_answer_case_1_3(stage,
                           request,
                           question_obj,
                           subject_obj,
                           student_obj,
                           question_id,
                           answer_text) -> Response:
    """
    :param stage: stage (case) of answer
    :param request:
    :param subject_name: subject name which one student applied
    :param question_id: question ID which question answered
    :param answer_text: student's answer to a question
    :return Response:
    """
    response = {
        'subject_name': subject_obj.full_name,
        'question_id': question_id,
        'student': question_obj.subject.full_name,
        'answer_text': answer_text
    }

    try:
        Answer.objects.create(
            subject=subject_obj,
            stage=stage,
            student=student_obj,
            question=question_obj,
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
