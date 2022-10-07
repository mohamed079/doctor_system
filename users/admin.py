from django.contrib import admin
from .models import ExtendUser
from django.contrib.auth.admin import UserAdmin



@admin.register(ExtendUser)
class CustomUserAdmin(UserAdmin):
    pass