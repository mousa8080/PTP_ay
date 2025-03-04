from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    national_id = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    is_driver = models.BooleanField(default=False)
    driver_photo = models.ImageField(upload_to='driver_photos/', null=True, blank=True)  # لازم يكون موجود  
    license_photo = models.ImageField(upload_to='license_photos/', null=True, blank=True)
    license_number = models.CharField(max_length=20, null=True, blank=True)  # رقم الرخصة

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'national_id']

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name


class DriverInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  driver_photo = models.ImageField(upload_to='driver_photos/', null=True, blank=True)
  license_photo = models.ImageField(upload_to='license_photos/', null=True, blank=True)
  liecense_number = models.CharField(max_length=24, null=True, blank=True)
  
  def __str__(self):
    return self.user.full_name