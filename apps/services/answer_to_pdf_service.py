# Python
import os
import pdfkit

pdfkit_config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')


def convert_answer_to_pdf(
        subject_code,
        subject_name,
        score,
        student_answer,
        teacher_name,
        output_file_name,
        hashed_student_id
):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    media_dir = os.path.join(base_dir, 'media', 'answers')

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            table, th, td {{
                border: 1px solid black;
                border-collapse: collapse;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
            }}
            .top1 {{
              width: 100%;
              text-align: center;
              font-weight: bold;
              border: 1px dashed;
            }}
            .top1 p span{{
              font-weight: 200;
            }}
    
        </style>
    </head>
    <body>
    <div class="top1">
            <p>Student: <span>{hashed_student_id}</span></p>
            <p>Subject:  <span> {subject_name} </span></p>
            <p>Student Score: <span>{score}</span></p>
            <br/>
            <p>Teacher's Fullname: {teacher_name}
            <p>Teacher sign: _____________</p>
          </div>
          {student_answer}
    </body>
    </html>
    """

    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8'
    }

    output_dir = os.path.join(media_dir, subject_code)
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f'{output_file_name}')

    pdfkit.from_string(html_content, str(output_path), options=options, configuration=pdfkit_config)

    relative_path = os.path.relpath(output_path, base_dir)
    return {
        'output_path': relative_path,
        'hashed_student_id': hashed_student_id
    }
