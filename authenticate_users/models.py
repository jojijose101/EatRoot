from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import check_password as django_check_password,make_password

# Create your models here.


CUSTOMER = "CUSTOMER"
HOTEL = "HOTEL"
DELIVERY = "DELIVERY"
ADMIN = "ADMIN"
    
ROLE_CHOICES = (
        (CUSTOMER, 'customer'),
        (HOTEL, 'hotel'),
        (DELIVERY, 'delivery'),
        (ADMIN, 'admin'),
    )

class User(AbstractUser):
    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default=ADMIN)


    def __str__(self):
        return f"{self.username}-{self.role}"


    



