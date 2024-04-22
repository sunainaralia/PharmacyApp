from django.db import models
from v1.api.account.models import User
import random
import string
from v1.api.patient.models import Patient
from v1.api.medical_side.models import MedicineModel


# Doctor model
class Doctor(models.Model):
    primary_id = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient_detail", primary_key=True
    )
    full_name = models.CharField(max_length=100)
    Mobile = models.IntegerField()
    dob = models.DateField()
    education = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="active")
    id_card = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    biography = models.TextField()
    profile_photo = models.CharField(max_length=1000, null=True)
    doctor_id = models.CharField(max_length=100, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job_time = models.CharField(max_length=100, default="full time")
    blood_group = models.CharField(max_length=100, default="o+")
    language = models.CharField(max_length=100, default="English")
    experience = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        if not self.doctor_id:
            self.doctor_id = self.generate_unique_id()
        super().save(*args, **kwargs)

    def generate_unique_id(self):
        length = 8
        alphanumeric = string.ascii_uppercase + string.digits
        return "".join(random.choice(alphanumeric) for _ in range(length))


# doctor experience
class DoctorExperience(models.Model):
    primary_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="doctor_experience"
    )
    institute_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    calculated_experience = models.CharField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        difference = self.job_end_date - self.job_start_date
        years = difference.days // 365
        months = (difference.days % 365) // 30
        if difference.days % 365 % 30 >= 20:
            months += 1
        self.calculated_experience = f"{years} years, {months} months"
        super().save(*args, **kwargs)


# PATIENT PRESCRIPTION
class Prescription(models.Model):
    written_by = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="prescription"
    )
    patient_id = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="prescription_of_doctor"
    )
    diagnosis = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    signature = models.CharField(max_length=100)
    insurance = models.CharField(max_length=100)
    address = models.TextField(null=True)


# PRESCRIPTION TABLET
class Prescription_tablet(models.Model):
    tablet_name = models.ForeignKey(
        MedicineModel, on_delete=models.CASCADE, related_name="prescribed_tablet"
    )
    course = models.CharField(max_length=100)
    tablet_duration = models.CharField(max_length=100)
    prescription = models.ForeignKey(
        Prescription, on_delete=models.CASCADE, related_name="prescriptionTablet"
    )


# APPOINTMENT MODEL
class Appointment(models.Model):
    patient_id = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="appointment"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)
    doctor_id = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="appointment_received",null=True
    )
    appointment_status = models.CharField(max_length=100,default='pending')
