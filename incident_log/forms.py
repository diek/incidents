from django import forms
from django.forms import ModelForm

from .models import IncidentReport


class DateInput(forms.DateInput):
    input_type = 'date'


class IncidentReportForm(ModelForm):
    class Meta:
        model = IncidentReport
        fields = [
            "shift",
            "time",
            "summary",
            "police_file_number",
            "merchandise_cost",
            "merchandise_description",
            "is_theft",
            "is_deterrence",
            "is_apprehension",
            "is_violence",
            "is_other",
            "suspect",
        ]
        widgets = {
            'time': DateInput(),
        }
