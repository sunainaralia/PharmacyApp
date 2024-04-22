from django.urls import path
from .views import PatientView
urlpatterns = [
    path("post-patient/", PatientView.as_view(), name="post patient"),
    path("post-patient/<pk>/", PatientView.as_view(), name="patient update"),
]
