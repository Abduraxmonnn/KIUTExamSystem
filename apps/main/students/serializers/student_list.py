# Rest-Framework
from rest_framework import serializers

# Project
from apps.main.exam_schedule.models import ExamSchedule
from apps.main.students.models import Student
from apps.main.subjects.models import Subject
from apps.main.student_groups.models import StudentGroup
from apps.main.answers.models import Answer

groups_picker = {
    'U': 'UZ',
    'R': 'RU',
    'E': 'EN',
    'K': 'KR'
}


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = [
            'id',
            'code',
        ]


class StudentSerializer(serializers.ModelSerializer):
    group = StudentGroupSerializer(many=False)

    class Meta:
        model = Student
        fields = [
            'id',
            'student_id',
            'full_name',
            'group',
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'id',
            'code',
            'full_name'
        ]


class ExamScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSchedule
        fields = [
            'start_time',
            'exam_date',
            'is_passed',
        ]


class StudentAnswerListSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False)
    subject = SubjectSerializer(many=False)
    exam_schedule = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = [
            'id',
            'student',
            'subject',
            'exam_schedule',
            'stage',
            'score'
        ]

    def get_exam_schedule(self, obj):
        try:
            exam_schedule = ExamSchedule.objects.get(
                subject=obj.subject,
                student=obj.student
            )
            return ExamScheduleSerializer(exam_schedule).data
        except ExamSchedule.DoesNotExist:
            return None
