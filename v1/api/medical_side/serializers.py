from rest_framework import serializers
from .models import MedicineModel


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineModel
        fields = '__all__'
