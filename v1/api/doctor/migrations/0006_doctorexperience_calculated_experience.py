# Generated by Django 5.0.4 on 2024-04-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_doctor_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorexperience',
            name='calculated_experience',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
