from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  national_id = models.CharField(max_length=14, unique=True)
  is_driver = models.BooleanField(db_default=False,null=True)
  phone=models.CharField(max_length=15,unique=True)






