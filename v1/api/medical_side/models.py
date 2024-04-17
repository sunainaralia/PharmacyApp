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
    rate = models.CharField(max_length=100)
    medicine_details = models.TextField()
