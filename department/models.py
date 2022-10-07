from turtle import update
from django.db import models

class Department (models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(default="" , null = True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name