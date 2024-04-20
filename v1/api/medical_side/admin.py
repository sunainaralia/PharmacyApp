from django.contrib import admin
from .models import MedicineModel, OrderItem, AddressModel, PharmacyModel


admin.site.register(PharmacyModel)
admin.site.register(MedicineModel)
admin.site.register(AddressModel)
admin.site.register(OrderItem)
