# Django
from django.urls import path

# Project
from apps.main.teachers.views import TeacherLogInAPIView, TeacherStudentsListViewSet, TeacherSetScoreViewSet, \
    TeacherWriteCommentViewSet, TeacherRetrieveCommentViewSet

urlpatterns = [
    path('login/', TeacherLogInAPIView.as_view()),
    path('students/list/', TeacherStudentsListViewSet.as_view({'post': 'create'})),
    path('students/make/score/', TeacherSetScoreViewSet.as_view({'post': 'create'})),
    path('students/create/comment/', TeacherWriteCommentViewSet.as_view({'post': 'create'})),
    path('students/retrieve/comment/', TeacherRetrieveCommentViewSet.as_view({'post': 'create'})),
]
