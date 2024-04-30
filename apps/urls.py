# Django
from django.urls import include, path

from apps.main.exam_schedule.views.login import LogInAPIView

urlpatterns = [
    path('login/', LogInAPIView.as_view()),

    path('answer/', include('apps.main.answers.urls')),
    path('exam_schedule/', include('apps.main.exam_schedule.urls')),
    path('questions/', include('apps.main.questions.urls')),
    path('students/', include('apps.main.students.urls')),
    path('subjects/', include('apps.main.subjects.urls')),
    path('teachers/', include('apps.main.teachers.urls')),
]
