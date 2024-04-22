from django.db import models
from v1.api.account.models import User
import random


class Patient(models.Model):
    primary_id = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient", primary_key=True
    )
    full_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    d_o_b = models.DateField()
    education = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100)
    address = models.TextField()
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    profile_img = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.CharField(max_length=100, null=True)
    patient_id = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        if self.patient_id is None:
            while True:
                random_id = random.randint(10000, 99999)
                if not Patient.objects.filter(patient_id=random_id).exists():
                    self.patient_id = random_id
                    break
        super().save(*args, **kwargs)
