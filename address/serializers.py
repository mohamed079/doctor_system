from .models import Address
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta :       
        model = Address
        fields = ("city" , "zone" , "street_name" , "building_number" , "flat_number" , "land_mark") 
        
    def create(self, validated_data ):
        address = Address.objects.create(
            user = validated_data["user"],
            city = validated_data["city"],
            zone = validated_data["zone"],
            street_name = validated_data["street_name"],
            building_number = validated_data["building_number"],
            flat_number = validated_data["flat_number"],
            land_mark = validated_data["land_mark"],

        )      
        return address  

