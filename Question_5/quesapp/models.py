from django.contrib.auth.base_user import AbstractBaseUser
from djongo import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    country = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"
