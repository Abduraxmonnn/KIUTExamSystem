# Django
from django.urls import path

# Project
from apps.main.answers.views import AnswerCreateAPIView, RetrieveCase2ScoreViewSet

urlpatterns = [
    path('create/', AnswerCreateAPIView.as_view({'post': 'create'})),
    path('retrieve/case2-score/', RetrieveCase2ScoreViewSet.as_view({'post': 'create'}))
]
