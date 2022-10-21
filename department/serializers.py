from importlib.metadata import requires
from unicodedata import name
from doctor.serializers import GeneralDoctorSerializer
from .models import Department
from rest_framework import serializers , validators
from address.serializers import GeneralDoctorAddressSerializer 

class DepartmentSerializer (serializers.ModelSerializer):
    doctors = GeneralDoctorSerializer(required = False, many = True)
    address = GeneralDoctorAddressSerializer(required = False, many = True)
    class Meta:
        model = Department
        fields = ("id" , "name" , "description" , "doctors" , "address")


class PrivateDepartmentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("name" , "description" )
        
    def create (self, validated_data ):
        department = Department.objects.create(
            name = validated_data["name"],
            description = validated_data["description"],
        )      
        return department

    
