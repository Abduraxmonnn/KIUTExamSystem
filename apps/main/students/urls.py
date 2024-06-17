# Django
from django.urls import include, path

# Rest-Framework
from rest_framework import routers

# Project
from apps.main.students.views import StudentAnswerListViewSet

router = routers.DefaultRouter()
router.register(r'list', StudentAnswerListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
