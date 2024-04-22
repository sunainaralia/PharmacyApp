
# Generated by Django 5.0.4 on 2024-04-18 06:03

# Generated by Django 5.0.4 on 2024-04-18 13:42


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=250, unique=True, verbose_name='Email')),
                ('user_name', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('role', models.CharField(default='user', max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
