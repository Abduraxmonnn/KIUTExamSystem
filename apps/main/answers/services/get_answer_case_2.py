# Python
import os
from fpdf import FPDF
import psycopg2
import datetime as dtime
import json

# Django
from django.db import connection as default_db

from apps.main.answers.models import Answer
# Project
from apps.services.create_case2_answer_pdf_service import CreateCase2AnswerPDFService, set_bold_font, \
    set_default_font, print_text, zipper, lock_pdf

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def create_pdf():
    pdf_file = FPDF('P', 'mm', (210, 297))
    font_dir = os.path.join(base_dir, 'static', 'fonts')
    default_font = os.path.join(font_dir, 'DejaVuSansMono.ttf')
    bold_font = os.path.join(font_dir, 'DejaVuSansMono-Bold.ttf')

    pdf_file.add_font(family='default', style='', fname=default_font, uni=True)
    pdf_file.add_font(family='default', style='B', fname=bold_font, uni=True)
    pdf_file.set_font(family='default', size=12)
    pdf_file.set_left_margin(5)
    pdf_file.set_right_margin(5)
    pdf_file.set_top_margin(5)
    pdf_file.set_auto_page_break(auto=True, margin=1)
    return pdf_file


class CreateCase2AnswerPDF:
    pdf_file = create_pdf()
    service = CreateCase2AnswerPDFService(pdf_file=pdf_file)

    query = """SELECT students_student.student_id, students_student.full_name, student_groups_studentgroup.code, directions_direction.code,
            directions_direction.name, subjects_subject.full_name, subjects_subject.code,teachers_teacher.full_name, score, answer_json, created_date from answers_answer
            join students_student on students_student.id = answers_answer.student_id
            join student_groups_studentgroup on students_student.group_id = student_groups_studentgroup.id
            join teachers_subjects_teachersubject on teachers_subjects_teachersubject.group_id = student_groups_studentgroup.id and
            answers_answer.subject_id = teachers_subjects_teachersubject.subject_id
            join teachers_teacher on teachers_subjects_teachersubject.teacher_id = teachers_teacher.id
            join subjects_subject on answers_answer.subject_id = subjects_subject.id
            join directions_direction on subjects_subject.direction_id = directions_direction.id
            where answers_answer.stage=2 and students_student.student_id = %s and subjects_subject.code = %s"""

    def __init__(self,
                 student_id: str = None,
                 subject_code: str = None,
                 language: str = None):
        self.student_id = student_id
        self.subject_code = subject_code
        self.language = language

    def generate_and_save_pdf(self):
        host = default_db.settings_dict['HOST']
        user = default_db.settings_dict['USER']
        password = default_db.settings_dict['PASSWORD']
        database = default_db.settings_dict['NAME']
        connection = psycopg2.connect(host=host, database=database, user=user, password=password)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(self.query, (self.student_id, self.subject_code))
        data = cursor.fetchone()

        self.pdf_file.add_page()

        if not data:
            return {
                'status': 'error',
                'message': 'connection to db is failed'
            }

        print_text(self.pdf_file, self.pdf_file.get_string_width('Student_id:') + 1, 7, "Student_id:",
                   ln=0,
                   align='L')
        set_bold_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width(data[0]) + 1, 7, data[0], ln=0, align='L')
        set_default_font(self.pdf_file)
        self.pdf_file.ln()
        print_text(self.pdf_file, self.pdf_file.get_string_width("Student's Fullname:") + 1, 7,
                   "Student's Fullname:", ln=0,
                   align='L')
        set_bold_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width(data[1]) + 1, 7, data[1], ln=0, align='L')
        self.pdf_file.ln()
        set_default_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width('Group:') + 1, 7, 'Group:', ln=0,
                   align='L')
        set_bold_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width(data[2]) + 1, 7, data[2], ln=0, align='L')
        self.pdf_file.ln()
        set_default_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width('Direction:') + 1, 7, 'Direction:', ln=0,
                   align='L')
        set_bold_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width(data[3] + "-" + data[4]) + 1, 7,
                   data[3] + "-" + data[4], ln=0,
                   align='L')
        self.pdf_file.ln()
        set_default_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width('Subject:') + 1, 7, 'Subject', ln=0,
                   align='L')
        set_bold_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width(data[5] + '-' + data[6]) + 1, 7,
                   data[5] + '-' + data[6], ln=0,
                   align='L')
        self.pdf_file.ln()
        set_default_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width("Teacher's Fullname:") + 1, 7,
                   "Teacher's Fullname:", ln=0,
                   align='L')
        set_bold_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width(data[7]) + 1, 7, data[7], ln=0, align='L')
        self.pdf_file.ln()
        set_default_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width('Score:') + 1, 7, 'Score:', ln=0,
                   align='L')
        set_bold_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width(str(data[8])) + 1, 7, str(data[8]), ln=0,
                   align='L')
        self.pdf_file.ln()
        set_default_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width('Created time of the document:') + 1, 7,
                   'Created time of the document:', ln=0, align='L')
        set_bold_font(self.pdf_file)
        print_text(self.pdf_file, self.pdf_file.get_string_width(
            dtime.date.today().strftime("%B %d, %Y") + ' // ' + dtime.datetime.now().strftime("%H:%M:%S")) + 1, 7,
                   str(dtime.date.today().strftime("%B %d, %Y") + ' // ' + dtime.datetime.now().strftime(
                       "%H:%M:%S")),
                   ln=0,
                   align='L')
        self.pdf_file.ln()
        x, y = self.service.add_image(self.pdf_file, os.path.join(base_dir, 'static/gray.jpg'))
        self.pdf_file.set_x(self.pdf_file.get_x() + x + 2)
        print_text(self.pdf_file, self.pdf_file.get_string_width(' - student picked') + 1, 7,
                   ' - student picked',
                   ln=0,
                   align='L')
        self.pdf_file.ln()
        x, y = self.service.add_image(self.pdf_file, os.path.join(base_dir, 'static/green.jpg'))
        self.pdf_file.set_x(self.pdf_file.get_x() + x + 2)
        print_text(self.pdf_file, self.pdf_file.get_string_width(' - correct answer') + 1, 7,
                   ' - correct answer',
                   ln=0,
                   align='L')
        self.pdf_file.ln()
        x, y = self.service.add_image(self.pdf_file, os.path.join(base_dir, 'static/red.jpg'))
        self.pdf_file.set_x(self.pdf_file.get_x() + x + 2)
        print_text(self.pdf_file, self.pdf_file.get_string_width(' - wrong answer') + 1, 7,
                   ' - wrong answer',
                   ln=0, align='L')
        self.pdf_file.ln()
        x, y = self.service.add_image(self.pdf_file, os.path.join(base_dir, 'static/rate.png'))
        self.pdf_file.set_x(self.pdf_file.get_x() + x + 2)
        print_text(self.pdf_file, self.pdf_file.get_string_width(" - question's rate") + 1, 7,
                   " - question's rate", ln=0,
                   align='L')
        self.pdf_file.ln()
        self.pdf_file.ln()
        self.pdf_file.set_x((self.pdf_file.w - self.pdf_file.l_margin - self.pdf_file.r_margin) / 2)
        print_text(self.pdf_file, self.pdf_file.get_string_width('TEST') + 1, 7, 'TEST', ln=0, align='C')
        self.pdf_file.ln()
        set_default_font(self.pdf_file)
        json_string = json.dumps(data[9], indent=4, ensure_ascii=False)
        # JSON stringni yana dictionary ga o'zgartirish
        json_data = json.loads(json_string)
        list_options = ['option1', 'option2', 'option3', 'option4']
        count = 1
        for question_id, question_data in json_data.items():
            for question in question_data['question']:
                for i in range(question['rate']):
                    x, y = self.service.add_image(self.pdf_file, os.path.join(base_dir, 'static/rate.png'))
                    self.pdf_file.set_x(self.pdf_file.get_x() + x + 1)
                variant = 0
                set_bold_font(self.pdf_file)
                print_text(self.pdf_file, self.pdf_file.get_string_width(str(count) + ". ") + 1, 7,
                           str(count) + ". ", ln=0,
                           align='L')
                for value in question["question"]:
                    if 'type' in value:
                        if value['type'] == 'text':
                            temp_list = self.service.sizer(self.pdf_file, [value['content'].split()])
                            for i in range(len(temp_list)):
                                print_text(self.pdf_file, 0, 7,
                                           zipper(temp_list[i]), ln=1, align='L')
                set_default_font(self.pdf_file)
                for option_key in list_options:
                    option = question[option_key]
                    if variant == 0:
                        char = 'A)'
                    elif variant == 1:
                        char = 'B)'
                    elif variant == 2:
                        char = 'C)'
                    else:
                        char = 'D)'
                    print_text(self.pdf_file, self.pdf_file.get_string_width(char) + 1, 7, char, ln=0,
                               align='L')
                    is_correct = option[-1]['correct']
                    if question_data['picked'] == option_key:
                        x, y = self.service.add_image(self.pdf_file, os.path.join(base_dir, 'static/gray.jpg'))
                        self.pdf_file.set_x(self.pdf_file.get_x() + x + 2)

                    if is_correct:
                        x, y = self.service.add_image(self.pdf_file, os.path.join(base_dir, 'static/green.jpg'))
                        self.pdf_file.set_x(self.pdf_file.get_x() + x + 2)
                    else:
                        x, y = self.service.add_image(self.pdf_file, os.path.join(base_dir, 'static/red.jpg'))
                        self.pdf_file.set_x(self.pdf_file.get_x() + x + 2)

                    for value in option:
                        if 'type' in value:
                            if value['type'] == 'text':
                                temp_list = self.service.sizer(self.pdf_file, [value['content'].split()])
                                for i in range(len(temp_list)):
                                    print_text(self.pdf_file, 0, 7,
                                               zipper(temp_list[i]), ln=1, align='L')
                    variant += 1
            count += 1
            self.pdf_file.ln()
            self.pdf_file.ln()

        answer_obj = Answer.objects.filter(subject__code=self.subject_code, student__student_id=self.student_id,
                                           stage=2).last()

        output_dir = (os.path.join(base_dir, 'media', 'case_2', self.subject_code))
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir,
                                   f"{answer_obj.question.language}_{answer_obj.subject.full_name}_{self.student_id}.pdf")
        self.pdf_file.output(name=f"{output_path}")
        relative_output_path = os.path.relpath(output_path, base_dir)
        # input_pdf_path = "new.pdf"
        # output_pdf_path = "new.pdf"
        # lock_pdf(input_pdf_path, output_pdf_path) agarda pdfni secure qilish kere bosa
        response = {
            "student_id": self.student_id,
            "subject": answer_obj.subject.full_name,
            "score": 2,
            "answer": relative_output_path
        }
        return {
            'status': 'successfully',
            'message': response
        }
