from django.db import models
from users.models import ExtendUser

class Address (models.Model):
    user = models.ForeignKey(ExtendUser,related_name='address',on_delete=models.CASCADE , null = True)
    city = models.CharField(max_length=20)
    zone = models.CharField(max_length=20)
    street_name = models.CharField(max_length=256)
    building_number = models.IntegerField(null=True , blank= True)
    flat_number = models.IntegerField(null=True , blank= True)
    land_mark = models.CharField(max_length=256 , null=True , blank= True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
