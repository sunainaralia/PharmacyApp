from rest_framework import serializers
from .models import (
    Doctor,
    DoctorExperience,
    Appointment,
    Prescription_tablet,
    Prescription,
)


# doctor serializers
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


# doctor experience serializers
class DoctorExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorExperience
        fields = "__all__"


# get all doctor serializers
class GetAllDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "profile_photo",
            "job_time",
            "full_name",
            "primary_id",
            "department",
            "designation",
        ]


# Appointment serializer
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


# prescription_tablet serializer
class PrescriptionTabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription_tablet
        fields = "__all__"


# Prescription serializer
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"
