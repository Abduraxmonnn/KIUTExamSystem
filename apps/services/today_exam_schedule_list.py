# # import psycopg2
# # from fpdf import FPDF
# # import datetime as dtime
# #
# # host = "127.0.0.1"
# # user = "master_sys_user"
# # password = 'master_12345'
# # database = 'master_sys_db_new'
# #
# #
# # def today_exam_schedule_list_service(rfid):
# #     connection = psycopg2.connect(host=host, database=database, user=user, password=password)
# #     connection.autocommit = True
# #     cursor = connection.cursor()
# #     cursor.execute("""SELECT students_student.full_name, subjects_subject.full_name,
# #                       login, password,  exam_date, room
# #                       FROM exam_schedule_examschedule
# #                       JOIN students_student ON exam_schedule_examschedule.student_id = students_student.id
# #                       JOIN subjects_subject ON subjects_subject.id = exam_schedule_examschedule.subject_id
# #                       WHERE DATE(exam_date) = %s and students_student.rfid = %s
# #                       ORDER BY to_char(exam_date, 'HH24:MI') ASC;""", (dtime.date.today(), rfid))
# #     data = cursor.fetchall()
# #     print(data)
# #     return data
# #
# #
# # today_exam_schedule_list_service(rfid="1234567000")
#
#
# import psycopg2
# import datetime as dtime
#
# host = "127.0.0.1"
# user = "master_sys_user"
# password = 'master_12345'
# database = 'master_sys_db'
# can_exam = False
#
#
# def rfid_get_status(rfid):
#     minutes_after = 10
#     minutes_before = 10
#     connection = psycopg2.connect(host=host, database=database, user=user, password=password)
#     connection.autocommit = True
#     cursor = connection.cursor()
#     cursor.execute("""SELECT students_student.full_name, subjects_subject.full_name,
#                       login, password,  exam_date, room
#                       FROM exam_schedule_examschedule
#                       JOIN students_student ON exam_schedule_examschedule.student_id = students_student.id
#                       JOIN subjects_subject ON subjects_subject.id = exam_schedule_examschedule.subject_id
#                       WHERE DATE(exam_date) = %s and students_student.rfid = %s
#                       ORDER BY to_char(exam_date, 'HH24:MI') ASC;""", (dtime.date.today(), rfid))
#     print(dtime.date.today())
#     data = cursor.fetchall()
#
#     return data
#
#
# rfid_get_status(rfid="1234567000")


import psycopg2
import datetime as dtime

host = "127.0.0.1"
user = "master_sys_user"
password = 'master_12345'
database = 'master_sys_db'


def rfid_get_status(rfid):
    connection = None
    try:
        # Connect to the database
        connection = psycopg2.connect(host=host, database=database, user=user, password=password)
        connection.autocommit = True
        cursor = connection.cursor()

        # Get current date
        current_date = dtime.date.today()
        print("Current Date:", current_date)
        print("RFID:", rfid)

        # Debug: Print the query and parameters
        query = """SELECT students_student.full_name, subjects_subject.full_name, 
                          login, password, exam_date, room
                          FROM exam_schedule_examschedule
                          JOIN students_student ON exam_schedule_examschedule.student_id = students_student.id 
                          JOIN subjects_subject ON subjects_subject.id = exam_schedule_examschedule.subject_id
                          WHERE DATE(exam_date) = %s AND students_student.rfid = %s
                          ORDER BY to_char(exam_date, 'HH24:MI') ASC;"""
        print("Query:", query)
        print("Parameters:", (current_date, rfid))

        # Execute the query
        cursor.execute(query, (current_date, rfid))

        # Fetch all results
        data = cursor.fetchall()
        print("Query Result:", data)

        return data
    except Exception as e:
        print("Error:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()


# Call the function
# rfid_get_status(rfid="1234567000")
