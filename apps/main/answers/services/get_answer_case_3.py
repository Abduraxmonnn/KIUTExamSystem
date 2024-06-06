# Rest-Framework
import os

from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

# Project
from apps.main.answers.models import Answer
from apps.services.load_json_to_cache_service import get_json_data_from_cache


def pdf_to_image_bytes(pdf_path):
    from pdf2image import convert_from_path

    pages = convert_from_path(pdf_path)

    # Save each page as a JPEG file using Pillow

    for i, page in enumerate(pages):
        page.save(f'page_{i}.jpg', 'JPEG')

    from pdf2image import convert_from_path
    import os

    # Create a folder to dump the jpegs
    os.makedirs("jpegs", exist_ok=True)

    pages = convert_from_path(pdf_path, first_page=1,
                              last_page=5, fmt='jpeg', output_file='page', paths_only=True,
                              output_folder="jpegs")

    return pages


def get_answer_from_db_to_case_3(subject_code, student_id, stage):
    try:
        answer_obj = Answer.objects.filter(subject__code=subject_code, student__student_id=student_id,
                                           stage=stage).last()
    except Exception as ex:
        return {
            'status': 'error',
            'message': f'{ex}'
        }

    if answer_obj is None:
        return {
            'status': 'error',
            'message': 'Answer does not Exists'
        }

    data = {
        'student_id': answer_obj.student.student_id,
        'subject': answer_obj.subject.full_name,
        'score': answer_obj.score,
        'questions': [],
        'answer_text': answer_obj.answer_text
    }

    file_path = answer_obj.question.file.name
    json_data = get_json_data_from_cache(file_path=file_path)

    if 'error' in json_data:
        return Response({
            'status': 'error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    for item in json_data:
        if int(item['id']) == int(answer_obj.question_ids):
            pdf_relative_path = item.get('content')
            pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_relative_path)
            images = pdf_to_image_bytes(pdf_path)
            item['images'] = images
            data['questions'].append(item)

    return {
        'status': 'successfully',
        'message': data
    }
