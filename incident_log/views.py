from django.urls import path

from . import views
from .views import IncidentCreateView

urlpatterns = [
    # path('', views.create_view, name='create_view'),
    path("incident/add/", IncidentCreateView.as_view(), name="incident-add",),
    path("time/", views.current_time, name="current_time"),
]
