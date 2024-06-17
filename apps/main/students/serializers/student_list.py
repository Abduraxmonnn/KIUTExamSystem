# Python
from collections import OrderedDict

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


def get_deepest_element(data):
    if isinstance(data, (tuple, list)):
        for item in data:
            result = get_deepest_element(item)
            if result is not None:
                return result
    else:
        return data
    return None


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
            'full_name',
            'stage',
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
    scores = serializers.CharField(read_only=True)
    exam_schedule = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = [
            'id',
            'student',
            'subject',
            'exam_schedule',
            'scores'
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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        answer_data = (
            Answer.objects
            .filter(
                subject__code=data['subject']['code'],
                student__student_id=data['student']['student_id'],
                question__language=groups_picker[data['student']['group']['code'][-1]]
            )
            .select_related('subject', 'subject__direction', 'student', 'student__direction',
                            'student__group', 'question', 'question__subject',
                            'question__subject__direction'))

        students_dict = {
            'case_1_score': None,
            'case_2_score': None,
            'case_3_score': None
        }

        for item in answer_data:
            students_dict[f'case_{item.stage}_score'] = item.score

        data['scores'] = students_dict
        return data

    @staticmethod
    def remove_duplicate_students(data):
        unique_entries = OrderedDict()
        for entry in data:
            student_subject_key = (entry['student']['student_id'], entry['subject']['id'])
            if student_subject_key not in unique_entries:
                unique_entries[student_subject_key] = entry
        return list(unique_entries.values())

    @classmethod
    def to_representation_list(cls, instances):
        serialized_data = [cls(instance).data for instance in instances]
        return cls.remove_duplicate_students(serialized_data)
