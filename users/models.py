from enum import unique
from multiprocessing.sharedctypes import Value
from operator import mod
from secrets import choice
from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser (AbstractUser):
    class Gender (models.Choices):
        MALE = "Male"
        FEMALE = "Female"

    class Type (models.IntegerChoices):
        USER = 1
        ADMIN = 2
        CUSTOMER_SERVICE = 3

    gender = models.CharField(choices=Gender.choices, default=Gender.MALE , max_length=6)
    age = models.DecimalField(max_digits=3 , decimal_places=0 , null=True , blank=True)
    phone_number = models.CharField(max_length=11 , null=True , blank=True , unique =True)
    birth_date = models.DateField(max_length=8 , null=True , blank=True)
    image = models.ImageField(upload_to = "photo%y%m%d" , null=True , blank=True)
    type = models.IntegerField(choices=Type.choices , default=Type.USER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



