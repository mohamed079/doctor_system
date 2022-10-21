from django.db import models
from doctor.models import Doctor
from users.models import ExtendUser
from address.models import Address

class Reservation (models.Model):

    class Status (models.Choices):
        PENDING = "Pending"
        ACCEPTANCE = "Acceptance"
        REJECTED = "Rejected"

    patient = models.ForeignKey(ExtendUser, related_name="reservations" , on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor , related_name="appointment" , on_delete=models.CASCADE)
    address = models.ForeignKey(Address , related_name="reservations" , on_delete=models.CASCADE , null =True) 
    description = models.TextField(default="" , null=True , blank= True)
    status = models.CharField(choices=Status.choices , default=Status.PENDING , max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




