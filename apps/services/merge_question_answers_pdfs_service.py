import os
import PyPDF2

from apps.services import convert_answer_to_pdf

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def merge_pdfs(
        subject_code,
        subject_name,
        student_id,
        student_score,
        student_answer,
        question_pdf_dir,
        teacher_name,
        language
):
    merger = PyPDF2.PdfMerger()

    try:
        output_dir = os.path.join(base_dir, 'media', 'merged', subject_code)
        os.makedirs(output_dir, exist_ok=True)

        convert_answer = convert_answer_to_pdf(subject_code, subject_name, student_id, student_score, student_answer,
                                               teacher_name=teacher_name, language=language)
        answer_pdf_path_absolute = os.path.join(base_dir, convert_answer['output_path'])
        merged_output_path = os.path.join(output_dir,
                                          f"{language}_{subject_name}_{convert_answer['hashed_student_id']}.pdf")

        question_pdf_dir = os.path.abspath(os.path.join(base_dir, question_pdf_dir.lstrip('/')))

        pdf_list = [question_pdf_dir, answer_pdf_path_absolute]  # files path must be absolute
        for pdf in pdf_list:
            if not os.path.exists(pdf):
                raise FileNotFoundError(f"PDF file does not exist: {pdf}")
            merger.append(pdf)

        with open(merged_output_path, 'wb') as output_file:
            merger.write(output_file)
    except FileNotFoundError:
        raise 'some PDF File does not exist'

    relative_output_path = os.path.relpath(merged_output_path, base_dir)
    return relative_output_path
