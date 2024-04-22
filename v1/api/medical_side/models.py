from django.db import models
from v1.api.account.models import User
from v1.api.patient.models import Patient
# MEDICAL MODEL
class MedicalModel(models.Model):
    primary_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='medical')
    medical_name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    profile_photo=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    gender=models.CharField(max_length=100)
    address=models.TextField()
    license_no=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    full_name=models.CharField(max_length=100)
    opening_schedule=models.TextField()


# # MEDICINE MODEL
class MedicineModel(models.Model):
    medical_id=models.ForeignKey(MedicalModel,on_delete=models.CASCADE,related_name='medicine_details')
    medicine_name = models.CharField(max_length=250)
    batch_number = models.CharField(max_length=250)
    manufactur_date = models.DateField()
    expiry_date = models.DateField()
    mfg_by = models.CharField(max_length=250)
    quantity = models.IntegerField()
    discount = models.CharField(max_length=25)
    gst = models.CharField(max_length=25)
    mrp = models.CharField(max_length=100)
    rate = models.IntegerField()
    medicine_details = models.TextField()
    available_sizes=models.CharField(max_length=100)
    delievery_charges=models.CharField(max_length=100)
    medicine_photo=models.CharField(max_length=100)
    packaging_fees=models.CharField(max_length=100)


# # ORDER MODEL
class OrderItem(models.Model):
    order_id = models.CharField(max_length=100)
    medicine = models.ForeignKey(
        MedicineModel, on_delete=models.CASCADE, related_name="order"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    quantity = models.IntegerField()
    delievery_method = models.CharField(max_length=100)
    reason=models.TextField()
    patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='Patient_order')



# class AddressModel(models.Model):
#     name = models.CharField(max_length=250)
#     email = models.EmailField()
#     phone_no = models.CharField(max_length=20)
#     address = models.CharField(max_length=250)
#     city = models.CharField(max_length=250)
#     landmark = models.CharField(max_length=250)
#     state = models.CharField(max_length=250)
#     zip_code = models.IntegerField()
#     alternate_phone_no = models.CharField(max_length=20, blank=True, null=True)
#     address_type = models.CharField(max_length=50)