from datetime import datetime

import pytz
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def validate_past_datetime(value):
    in_date = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    now = pytz.utc.localize(now)
    in_date = pytz.utc.localize(in_date)
    if in_date > now:
        raise ValidationError("Cannot be in the future.")


class Shift(models.Model):
    class ShiftChoice(models.TextChoices):
        MORNING = "M", _("Morning")
        AFTERNOON = "A", _("Afternoon")
        OVERNIGHT = "O", _("Overnight")

    name = models.CharField(
        max_length=1, choices=ShiftChoice.choices, default=ShiftChoice.AFTERNOON,
    )

    def __str__(self):
        display_value = self.get_name_display()
        return "{}".format(display_value)


class IncidentReport(models.Model):
    shift = models.ForeignKey(Shift, models.PROTECT, related_name="incident_reports")
    time = models.DateTimeField(validators=[validate_past_datetime])
    summary = models.TextField()
    police_file_number = models.CharField(max_length=16, blank=True)
    merchandise_cost = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    merchandise_description = models.TextField(blank=True)

    is_theft = models.BooleanField("Theft", default=False)
    is_deterrence = models.BooleanField("Deterrence", default=False)
    is_apprehension = models.BooleanField("Apprehension", default=False)
    is_violence = models.BooleanField("Violence", default=False)
    is_other = models.BooleanField(
        "Other", default=False, help_text="Explain in summary"
    )

    suspect = models.CharField(max_length=120, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
