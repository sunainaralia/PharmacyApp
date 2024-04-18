from .models import AddressModel, OrderItem, MedicineModel
from rest_framework import serializers


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineModel
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
