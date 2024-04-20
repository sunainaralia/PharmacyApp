
from rest_framework import serializers
from .models import Doctor, DoctorExperience


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
