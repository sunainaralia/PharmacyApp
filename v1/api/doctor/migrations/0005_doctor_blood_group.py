# Generated by Django 5.0.4 on 2024-04-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_doctor_job_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='blood_group',
            field=models.CharField(default='o+', max_length=100),
        ),
    ]
