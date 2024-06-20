# Python
from PyPDF2 import PdfWriter, PdfReader
from fpdf import FPDF
from PIL import Image


def set_bold_font(pdf_file: FPDF):
    pdf_file.set_font(family='default', style='B', size=12)


def set_default_font(pdf_file: FPDF):
    pdf_file.set_font(family='default', style='', size=12)


def print_text(pdf_file: FPDF, w, h, text, ln, align):
    pdf_file.cell(w=w, h=h, txt=text, align=align, ln=ln)


def zipper(list_of_words):
    temp_str = str()
    for word in list_of_words:
        temp_str = temp_str + word + ' '
    temp_str = temp_str[:-1]
    return temp_str


def lock_pdf(input_pdf, output_pdf):
    pdf_writer = PdfWriter()

    pdf_reader = PdfReader(input_pdf)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(user_password='', use_128bit=True, permissions_flag=0)

    with open(output_pdf, "wb") as out_pdf:
        pdf_writer.write(out_pdf)


class CreateCase2AnswerPDFService:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file

    def sizer(self, pdf_file: FPDF, words: list):
        for i in range(len(words) - 1, -1, -1):
            if pdf_file.get_string_width(
                    zipper(words[i])) > pdf_file.w - pdf_file.r_margin - pdf_file.l_margin - pdf_file.get_x():
                if len(words[i]) == 1:
                    continue
                if i + 1 == len(words):
                    temp = list()
                    temp.append(words[i][-1])
                    words.append(temp)
                    words[i].pop()
                    self.sizer(pdf_file, words)
                else:
                    words[i + 1].insert(0, words[i][-1])
                    words[i].pop()
                    self.sizer(pdf_file, words)
        return words

    def add_image(self, pdf_file: FPDF, image_path: str):
        img = Image.open(image_path)
        img_width, img_height = img.size
        img_width_mm = img_width * 0.264583
        img_height_mm = img_height * 0.264583
        pdf_file.image(image_path, x=self.pdf_file.get_x(), y=self.pdf_file.get_y() + 1, w=img_width_mm,
                       h=img_height_mm)
        return img_width_mm, img_height_mm
