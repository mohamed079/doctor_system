from django.db import models
from doctor.models import Doctor
from patient.models import Patient
from payment.models import Payment

class Reservation (models.Model):

    class Status (models.Choices):
        pending = "1"
        acceptance = "2"
        rejected = "3"

    patient = models.ForeignKey(Patient , related_name="reservations" , on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor , related_name="reservations" , on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment , related_name="reservations" , on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    description = models.TextField(default="" , null=True , blank= True)
    is_paid = models.BooleanField()
    status = models.CharField(choices=Status.choices , default=Status.pending , max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




