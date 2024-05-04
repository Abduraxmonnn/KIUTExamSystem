# Django
from django.urls import path

# Project
from apps.main.answers.views import AnswerCreateAPIView

urlpatterns = [
    path('create/', AnswerCreateAPIView.as_view({'post': 'create'}))
]
