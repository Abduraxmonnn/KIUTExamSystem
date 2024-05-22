# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question
from apps.main.subjects.models import Subject
from apps.services.get_user_by_token_service import get_student_by_token
from apps.services.load_json_to_cache_service import get_json_data_from_cache


def create_answer_to_db_case_2(
        model,
        request,
        stage,
        question_id,
        subject_name,
        picked):
    try:
        get_student = get_student_by_token(request)
        get_question = Question.objects.get(subject__full_name=subject_name, stage=stage)
        get_subject = Subject.objects.get(full_name=subject_name)
    except Exception as ex:
        print('---------> 33 line: create_answer_service: ', ex)
        return Response({
            'status': 'error',
            'message': 'Student / Question / Subject Does Not Exists or Error!'
        }, status=status.HTTP_400_BAD_REQUEST)

    file_path = get_question.file.name
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

    existing_answer = model.objects.filter(
        student=get_student,
        subject=get_subject,
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
        created_answer = model.objects.create(
            subject=get_subject,
            stage=stage,
            question=get_question,
            student=get_student,
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
