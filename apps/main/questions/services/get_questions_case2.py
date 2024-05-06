# Python
import os
import json
import random
from typing import TypeVar

# Rest-Framework
from rest_framework import status
from rest_framework.response import Response

# Project
from apps.main.questions.models import Question
from django.conf import settings

T = TypeVar('T')


def get_question_case_1(subject: T, stage: T, num_questions: int = 5) -> Response:
    ...
