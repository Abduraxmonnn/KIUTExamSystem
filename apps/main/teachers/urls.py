# Django
from django.urls import path

# Project
from apps.main.teachers.views import TeacherLogInAPIView, TeacherStudentsListViewSet, TeacherStudentsMaseScoreViewSet

urlpatterns = [
    path('login/', TeacherLogInAPIView.as_view()),
    path('students/list/', TeacherStudentsListViewSet.as_view({'post': 'create'})),
    path('students/make/score/', TeacherStudentsMaseScoreViewSet.as_view({'post': 'create'}))
]
