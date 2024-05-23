# Django
from django.urls import include, path

# Project
from apps.main.teachers.views.techer_login import TeacherLogInAPIView

urlpatterns = [
    path('login/', TeacherLogInAPIView.as_view())
]
