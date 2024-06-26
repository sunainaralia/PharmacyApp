# Generated by Django 5.0.4 on 2024-04-18 13:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('primary_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='patient_detail', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('full_name', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField()),
                ('dob', models.DateField()),
                ('education', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('avatar', models.CharField(max_length=100)),
                ('status', models.CharField(default='active', max_length=100)),
                ('id_card', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('marital_status', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('profile_photo', models.CharField(max_length=1000, null=True)),
                ('doctor_id', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
