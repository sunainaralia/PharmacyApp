from django.db import models


class MedicineModel(models.Model):
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


STATE_CHOICES = {
    "Andhra_Pradesh": "Andhra_Pradesh",
    "Arunachal_Pradesh": "Arunachal_Pradesh",
    "Assam": "Assam",
    "Bihar": "Bihar",
    "Chhattisgarh": "Chhattisgarh",
    "Goa": "Goa",
    "Gujarat": "Gujarat",
    "Haryana": "Haryana",
    "Himachal_Pradesh": "Himachal_Pradesh",
    "Jharkhand": "Jharkhand",
    "Karnataka": "Karnataka",
    "Kerala": "Kerala",
    "Madhya": "Madhya",
    "Maharashtra": "Maharashtra",
    "Manipur": "Manipur",
    "Meghalaya": "Meghalaya",
    "Mizoram": "Mizoram",
    "Nagaland": "Nagaland",
    "Odisha": "Odisha",
    "Punjab": "Punjab",
    "Rajasthan": "Rajasthan",
    "Sikkim": "Sikkim",
    "Tamil": "Tamil",
    "Telangana": "Telangana",
    "Tripura": "Tripura",
    "Uttar_Pradesh": "Uttar_Pradesh",
    "Uttarakhand": "Uttarakhand",
    "West Bengal": "West Bengal",
    "Andaman_and_Nicobar_Islands": "Andaman_and_Nicobar_Islands",
    "Chandigarh": "Chandigarh",
    "Dadra_and_Nagar_Haveli_Daman_and_Diu": "Dadra_and_Nagar_Haveli_Daman_and_Diu",
    "Jammu_and_Kashmir": "Jammu_and_Kashmir",
    "Ladakh": "Ladakh",
    "Lakshadweep": "Lakshadweep",
    "Delhi": "Delhi",
    "Puducherry": "Puducherry",
}


ADDRESS_TYPE = {
    'Home': 'Home',
    'Office': 'Office',
}
class AddressModel(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    landmark = models.CharField(max_length=250)
    state = models.CharField(choices=STATE_CHOICES, max_length=250)
    zip_code = models.IntegerField()
    alternate_phone_no = models.CharField(max_length=20, blank=True, null=True)
    address_type = models.CharField(choices=ADDRESS_TYPE, max_length=50)


ORDER_STATUS = {
    'Pending': 'Pending',
    'Confirm': 'Confirm',
    'Shipped': 'Shipped',
    'OutofDelivered': 'Out of Delivered',
    'Delivered': 'Delivered',
    'Cancelle': 'Cancelled'
}


class OrderItem(models.Model):
    addresses = models.ForeignKey(AddressModel, on_delete=models.CASCADE)
    medicine = models.ForeignKey(MedicineModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def subtotal(self):
        return self.quantity * self.medicine.rate
