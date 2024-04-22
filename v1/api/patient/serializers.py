from rest_framework import serializers
from .models import Patient


# seriailizer for patient
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
