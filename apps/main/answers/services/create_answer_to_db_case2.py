# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.answers.models import Answer
from apps.services.load_json_to_cache_service import get_json_data_from_cache


def create_answer_to_db_case_2(
        request,
        stage,
        student_obj,
        question_obj,
        question_id,
        subject_obj,
        picked) -> Response:
    file_path = question_obj.file.name
    json_data = get_json_data_from_cache(file_path=file_path)

    if 'error' in json_data:
        return Response({
            json_data
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    valid_questions = [item for item in json_data if 'question' in item]

    question = {
        f'question_id__{question_id}': {
            'question': [],
            'picked': picked,
            'is_true': False
        }
    }

    existing_answer = Answer.objects.filter(
        student=student_obj,
        subject=subject_obj,
        stage=stage,
    ).first()

    is_correct = False
    if question_id:
        for item in valid_questions:
            if int(question_id) == item['id']:
                is_picked = item[picked][-1]['correct']
                question[f'question_id__{question_id}']['question'].append(item)
                question[f'question_id__{question_id}']['is_true'] = is_picked
                is_correct = is_picked
                break

    if not existing_answer:
        created_answer = Answer.objects.create(
            subject=subject_obj,
            stage=stage,
            question=question_obj,
            student=student_obj,
            answer_json=question
        )
        obj = created_answer
    else:
        tmp_answer_json = existing_answer.answer_json
        obj = existing_answer

        tmp_answer_json[f'question_id__{question_id}'] = question[f'question_id__{question_id}']

    if is_correct:
        obj.score += 1

    obj.save()

    if not question[f'question_id__{question_id}']['question']:
        return Response({
            'status': 'error',
            'message': 'Question ID incorrect, Please Check and Try Again!'
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        'status': 'successfully',
        'message': question
    }, status=status.HTTP_200_OK)

