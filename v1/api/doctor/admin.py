from django.contrib import admin
from .models import Doctor,DoctorExperience

# admin register of doctor model
class DoctorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Doctor._meta.fields]


admin.site.register(Doctor, DoctorAdmin)
class DoctorExperienceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DoctorExperience._meta.fields]


admin.site.register(DoctorExperience, DoctorExperienceAdmin)
