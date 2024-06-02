# Django
from django.urls import path

# Project
from apps.main.teachers.views import TeacherLogInAPIView, TeacherStudentsListViewSet, TeacherSetScoreViewSet

urlpatterns = [
    path('login/', TeacherLogInAPIView.as_view()),
    path('students/list/', TeacherStudentsListViewSet.as_view({'post': 'create'})),
    path('students/make/score/', TeacherSetScoreViewSet.as_view({'post': 'create'})),
]
