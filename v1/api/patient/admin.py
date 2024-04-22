from django.contrib import admin
from .models import Patient


# patient admin
class PatientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Patient._meta.fields]


admin.site.register(Patient, PatientAdmin)
