from email.policy import default
from django.db import models
from users.models import ExtendUser
from department.models import Department
from users.models import ExtendUser
class Doctor (ExtendUser):
    description = models.TextField(default="")
    degree = models.CharField(max_length=256)
    department = models.ForeignKey(Department , related_name="doctors" , on_delete=models.CASCADE)
    fees = models.DecimalField(max_digits=4 , decimal_places=0)


    