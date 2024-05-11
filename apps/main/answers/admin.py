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
    list_display = ['id', 'subject', 'stage', 'student', 'question', 'score', 'created_date']
    list_display_links = ['subject', 'student']
    readonly_fields = ('pretty_json', )
    exclude = ('answer_json', )

    def pretty_json(self, instance):
        """Function to display pretty version of our data"""

        # Convert the data to sorted, indented JSON
        response = json.dumps(instance.answer_json, sort_keys=True, indent=2)  # <-- your field here

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
