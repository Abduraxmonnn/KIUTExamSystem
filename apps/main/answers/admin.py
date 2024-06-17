# Django
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

# Django
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

# Project
from apps.main.answers.models import Answer


@admin.register(Answer)
class AnswerAdmin(ModelAdmin):
    list_display = ['id', 'subject', 'get_subject_code', 'stage', 'get_student_id', 'get_student_group',
                    'get_question_lang', 'question', 'score', 'created_date']
    # list_filter = ['stage']
    list_display_links = ['get_subject_code', 'get_student_id']
    search_fields = ['student__student_id']
    readonly_fields = ('pretty_json',)
    exclude = ('answer_json',)

    def get_student_id(self, obj):
        return obj.student.student_id

    def get_subject_code(self, obj):
        return obj.subject.code

    def get_question_lang(self, obj):
        return obj.question.language

    def get_student_group(self, obj):
        return obj.student.group

    def pretty_json(self, instance):
        """Function to display pretty version of our data"""

        # Convert the data to sorted, indented JSON
        response = json.dumps(instance.answer_json, sort_keys=True, indent=2, ensure_ascii=False)  # <-- your field here

        # Truncate the data. Alter as needed
        response = response[:5000]

        # Get the Pygments formatter
        formatter = HtmlFormatter(style='colorful')

        # Highlight the data
        response = highlight(response, JsonLexer(), formatter)

        # Get the stylesheet
        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        # Safe the output
        return mark_safe(style + response)

    pretty_json.short_description = 'Pretty json'
