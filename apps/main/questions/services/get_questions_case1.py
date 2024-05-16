# Python
import os
import json
import random
import requests
from typing import TypeVar

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question

from apps.services.get_user_by_token_service import get_student_by_token
from apps.services.load_json_to_cache_service import get_json_data_from_cache

T = TypeVar('T')


def get_question_case_1(
        request: requests,
        subject: T,
        stage: T,
        question_id: T = None,
        num_questions: int = 5) -> Response:

    groups_picker = {
        'U': 'UZ',
        'R': 'RU',
        'E': 'EN',
        'K': 'KR'
    }

    try:
        student_group_letter = get_student_by_token(request).group.code[-1]
        get_question = Question.objects.get(
            subject__full_name=subject,
            stage=stage,
            language=groups_picker[student_group_letter])
    except Exception as ex:
        print('---------> 42 line: get_question_case1_service: ', ex)
        return Response({
            'status': 'error',
            'message': f'Student / Question Does Not Exists or Error! {ex}'
        }, status=status.HTTP_400_BAD_REQUEST)

    file_path = get_question.file.name
    json_data = get_json_data_from_cache(file_path=file_path)

    if 'error' in json_data:
        return Response({
            json_data
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    result = {
        'specialization': get_question.specialization,
        'language': get_question.language,
        'academic_semester': get_question.academic_semester,
        'questions': []
    }
    valid_questions = [item for item in json_data if 'question' in item]

    if question_id:
        for item in valid_questions:
            if int(question_id) == item['id']:
                result['questions'].append(item)
                break

    while len(result['questions']) < num_questions:
        remaining_candidates = [q for q in valid_questions if q not in result['questions']]
        random_question = random.choice(remaining_candidates)
        result['questions'].append(random_question)

    return Response({
        'status': 'successfully',
        'message': result
    }, status=status.HTTP_200_OK)
