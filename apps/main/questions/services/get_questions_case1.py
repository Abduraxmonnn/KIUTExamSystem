# Python
import os
import json
import random
from typing import TypeVar

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question
from django.conf import settings

T = TypeVar('T')


def get_question_case_1(subject: T, stage: T, question_id: T = None, num_questions: int = 5) -> Response:
    get_question = Question.objects.get(subject__full_name=subject, stage=stage)
    file_path = get_question.file.name
    try:
        absolute_file_path = os.path.join(settings.MEDIA_ROOT, file_path)
        with open(absolute_file_path, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        return Response({
            'status': 'error',
            'message': 'File Does Not Exist!'
        }, status=status.HTTP_404_NOT_FOUND)

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
