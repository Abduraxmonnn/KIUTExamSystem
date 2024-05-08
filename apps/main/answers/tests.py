from django.test import TestCase

# Create your tests here.
data = {"question_id__111": {"picked": "option3", "is_true": true, "question": [
    {"id": 111, "rate": 1,
     "option1": [{"type": "text", "content": " Ishlab chiqarish tezligini oshirish\n"}, {"correct": false}],
     "option2": [{"type": "text", "content": " Energiya sarfini kamaytirish\n"}, {"correct": false}],
     "option3": [{"type": "text", "content": " Robotlarga murakkab vazifalarni mustaqil bajarish imkonini berish\n"},
                 {"correct": true}],
     "option4": [{"type": "text", "content": " Robotlarni arzonlashtirish\n"}, {"correct": false}],
     "question": [{"type": "text", "content": " Robototexnikada sun' iy aqlning asosiy maqsadi nima?\n"}]}]},
        "question_id__120": {"picked": "option3", "is_true": false, "question": [
            {"id": 120, "rate": 1,
             "option1": [{"type": "text", "content": " Eng kam xotira sarflaydigan yo' lni topish\n"},
                         {"correct": false}],
             "option2": [{"type": "text", "content": " Ikki nuqta orasidagi eng qisqa yo' lni topish\n"},
                         {"correct": true}],
             "option3": [{"type": "text", "content": " Noma' lum hududning xaritasini yaratish\n"}, {"correct": false}],
             "option4": [
                 {"type": "text", "content": " Robotning maksimal batareya quvvatidan foydalanishini ta' minlash\n"},
                 {"correct": false}],
             "question": [{"type": "text", "content": " A-star algoritmining asosiy maqsadi nima?\n"}]}]},
        "question_id__166": {"picked": "option1", "is_true": true, "question": [{"id": 166, "rate": 2, "option1": [
            {"type": "text",
             "content": " Ular konvolutsion qatlamlardagi umumiy vaznlar tufayli o' qitish uchun kamroq parametrlarni talab qiladi\n"},
            {"correct": true}], "option2": [{"type": "text", "content": " Dasturlash osonroq\n"}, {"correct": false}],
                                                                                 "option3": [{"type": "text",
                                                                                              "content": " Kamroq energiya iste' mol qiladi\n"},
                                                                                             {"correct": false}],
                                                                                 "option4": [{"type": "text",
                                                                                              "content": " Kichikroq o' lchamga ega\n"},
                                                                                             {"correct": false}],
                                                                                 "question": [{"type": "text",
                                                                                               "content": " Robotikada vizual ma' lumotlarni qayta ishlashda CNNlar an' anaviy neyron tarmoqlariga qaraganda qanday afzallikka ega?\n"}]}]}}
