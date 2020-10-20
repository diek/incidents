from django.contrib import admin

from .models import IncidentReport, Shift

admin.site.register(IncidentReport)
admin.site.register(Shift)
