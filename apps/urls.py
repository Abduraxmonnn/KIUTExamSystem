# Django
from django.urls import include, path

urlpatterns = [
    path('answer/', include('apps.answers.urls')),
    path('exam_schedule/', include('apps.exam_schedule.urls')),
    path('questions/', include('apps.questions.urls')),
    path('students/', include('apps.students.urls')),
    path('subjects/', include('apps.subjects.urls')),
    path('teachers/', include('apps.teachers.urls')),
]
