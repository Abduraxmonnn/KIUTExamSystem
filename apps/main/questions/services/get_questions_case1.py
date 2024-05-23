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


def get_question_case_1_3(
        request: requests,
        question_obj: T,
        stage: T,
        question_id: T = None,
        num_questions: int = 5) -> Response:

    file_path = question_obj.file.name
    json_data = get_json_data_from_cache(file_path=file_path)

    if 'error' in json_data:
        return Response({
            json_data
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    result = {
        'specialization': question_obj.specialization,
        'language': question_obj.language,
        'academic_semester': question_obj.academic_semester,
        'questions': []
    }

    if stage == 1:
        valid_questions = [item for item in json_data if 'question' in item]
        if question_id:
            for item in valid_questions:
                if int(question_id) == item['id']:
                    result['questions'].append(item)
                    break
    elif stage == 3:
        num_questions = 1
        valid_questions = [item for item in json_data if 'content' in item]
    else:
        valid_questions = []

    while len(result['questions']) < num_questions:
        remaining_candidates = [q for q in valid_questions if q not in result['questions']]
        random_question = random.choice(remaining_candidates)
        result['questions'].append(random_question)

    return Response({
        'status': 'successfully',
        'message': result
    }, status=status.HTTP_200_OK)
