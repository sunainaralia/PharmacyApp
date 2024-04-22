from django.urls import path
from .views import (
    PostDoctorView,
    PostDoctorExperienceView,
    EditDoctorView,
    AppointmentView,
    GetDoctorWithAppointment,
)

urlpatterns = [
    path("post-doctor-details/", PostDoctorView.as_view(), name="doctor detail"),
    path(
        "post-doctor-experience/",
        PostDoctorExperienceView.as_view(),
        name="doctor experience",
    ),
    path(
        "edit-doctor/<pk>/",
        EditDoctorView.as_view(),
        name="EditDoctor",
    ),
    path(
        "edit-doctor/",
        EditDoctorView.as_view(),
        name="EditDoctor",
    ),
    path(
        "post-appointment/",
        AppointmentView.as_view(),
        name="postAppointment",
    ),
    path(
        "get-doctor-appointment/<pk>/",
        GetDoctorWithAppointment.as_view(),
        name="getdoctorandappointments",
    ),
]
