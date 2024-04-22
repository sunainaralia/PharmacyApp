from django.contrib import admin
from .models import (
    Doctor,
    DoctorExperience,
    Prescription,
    Prescription_tablet,
    Appointment,
)


# admin register of doctor model
class DoctorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Doctor._meta.fields]


admin.site.register(Doctor, DoctorAdmin)


# admin of doctor experience
class DoctorExperienceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DoctorExperience._meta.fields]


admin.site.register(DoctorExperience, DoctorExperienceAdmin)


# admin of Prescription
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Prescription._meta.fields]


admin.site.register(Prescription, PrescriptionAdmin)


# admin of Prescription_tablet
class Prescription_tabletAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Prescription_tablet._meta.fields]


admin.site.register(Prescription_tablet, Prescription_tabletAdmin)


# admin of Appointment
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Appointment._meta.fields]


admin.site.register(Appointment, AppointmentAdmin)
