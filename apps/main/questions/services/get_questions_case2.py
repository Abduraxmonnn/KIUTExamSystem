# Python
import random

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question
from apps.services.load_json_to_cache_service import get_json_data_from_cache


def get_question_case_2(subject_name, stage, file_path, question_id=None, num_questions: int = 20) -> Response:
    try:
        # Convert question_id to integer if provided
        question_id_int = int(question_id) if question_id is not None else None

        # Retrieve question based on subject_name and stage
        get_question = Question.objects.get(subject__full_name=subject_name, stage=stage)

        json_data = get_json_data_from_cache(file_path=file_path)

        if 'error' in json_data:
            return Response({
                        json_data
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Filter valid questions with rates from JSON data
        valid_questions = [item for item in json_data if 'rate' in item]

        # Define target rates and initialize rate counters
        target_rates = {1: 5, 2: 8, 3: 7}
        rates = {1: 0, 2: 0, 3: 0}

        # Prepare result list to collect selected questions
        result = {
            'specialization': get_question.specialization,
            'language': get_question.language,
            'academic_semester': get_question.academic_semester,
            'questions': []
        }

        if question_id_int is not None:
            specific_question = next((item for item in json_data if item.get('id') == question_id_int), None)
            if specific_question:
                result['questions'].append(specific_question)
            else:
                return Response({
                    'status': 'error',
                    'message': f'Question with id {question_id} not found'
                }, status=status.HTTP_404_NOT_FOUND)

            return Response({
                'status': 'successfully',
                'message': result
            }, status=status.HTTP_200_OK)
        else:

            # Iterate through valid_questions and prioritize based on rates
            for item in valid_questions:
                rate = item.get('rate', None)
                if rate in target_rates and rates[rate] < target_rates[rate]:
                    result['questions'].append(item)
                    rates[rate] += 1

            # Check if we have collected enough questions, adjust if necessary
            while len(result['questions']) < num_questions:
                # Randomly pick a question from valid_questions to complete the count
                remaining_candidates = [q for q in valid_questions if q not in result['questions']]
                random_question = random.choice(remaining_candidates)
                result['questions'].append(random_question)

            # Shuffle the final list of questions for randomness
            random.shuffle(result['questions'])

            return Response({
                'status': 'successfully',
                'message': result
            }, status=status.HTTP_200_OK)

    except Question.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Question not found for the specified subject and stage'
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({
            'status': 'error',
            'message': f'Error: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
