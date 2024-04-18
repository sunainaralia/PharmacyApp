from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def _create_user(
        self,
        email,
        password,
        password2=None,**extra_fields,
    ):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        try:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        except:
            raise

    def create_user(self, email, password=None,password2=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)
        return self._create_user(email, password=password, **extra_fields)


# Custom User
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=250,
        unique=True
    )
    user_name = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_blocked = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role=models.CharField(max_length=300,default='user')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class Doctor(models.Model):
    primary_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name="patient_detail",primary_key=True)
    full_name=models.CharField(max_length=100)
    Mobile=models.IntegerField()
    dob=models.DateField()
    education=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    avatar=models.CharField(max_length=100)
    status=models.CharField(default='active')
    id_card = models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    religion=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    marital_status=models.CharField(max_length=100)
    biography=models.CharField(max_length=100)

