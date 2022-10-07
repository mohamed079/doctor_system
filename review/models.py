from operator import mod
from django.db import models
from users.models import ExtendUser

class Review (models.Model):
    user = models.ForeignKey(ExtendUser,related_name='review',on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=5,decimal_places=0)
    feedback = models.TextField(null=True , blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

