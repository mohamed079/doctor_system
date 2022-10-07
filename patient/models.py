from django.db import models
from users.models import ExtendUser
class Patient (ExtendUser):
    whatsApp_number = models.CharField(max_length=13 , null=True , blank=True)