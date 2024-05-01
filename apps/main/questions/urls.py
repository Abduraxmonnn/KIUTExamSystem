# Django
from django.urls import path

# Project
from apps.main.questions.views import QuestionRetrieveAPIView

urlpatterns = [
    path('retrieve/', QuestionRetrieveAPIView.as_view())
]
