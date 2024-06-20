# Rest-Framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Project
from apps.main.answers.models import Answer
from apps.main.students.serializers import StudentAnswerListSerializer
from apps.custom_pagination.standard_pagination import StandardResultsSetPagination


class StudentAnswerListViewSet(ModelViewSet):
    queryset = (
        Answer.objects.all()
        .select_related('subject', 'subject__direction', 'student', 'student__direction',
                        'student__group', 'question', 'question__subject',
                        'question__subject__direction')
    )
    serializer_class = StudentAnswerListSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = [
        'student__student_id',
        'student__full_name',
        'subject__full_name',
        'subject__code',

    ]

    ordering_fields = ['student__full_name', 'subject__full_name', '-id']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_data = self.get_paginated_response(serializer.data)
            # Use to_representation_list to remove duplicates
            paginated_data.data['results'] = StudentAnswerListSerializer.remove_duplicate_students(
                paginated_data.data['results'])
            return paginated_data

        serializer = self.get_serializer(queryset, many=True)
        data = StudentAnswerListSerializer.to_representation_list(queryset)
        return Response(data)
