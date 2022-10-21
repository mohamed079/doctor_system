from .models import Reservation
from rest_framework import serializers
from doctor.serializers import GeneralDoctorSerializer
from patient.serializers import PatientSerializer

class ReservationSerializer(serializers.ModelSerializer):
    class Meta :       
        model = Reservation
        fields = ("description",) 
        
    def create(self, validated_data ):
        reservation = Reservation.objects.create(
            patient = validated_data["patient"],
            doctor = validated_data["doctor"],
            address = validated_data["address"],
            description = validated_data["description"],
        )      
        return reservation  

class PatientReservationSerializer(serializers.ModelSerializer):
    doctor = GeneralDoctorSerializer(read_only=True)
    address = serializers.SlugRelatedField(read_only=True, slug_field='zone')
    class Meta :       
        model = Reservation
        fields = ("doctor" , "address" ,"description","status") 

class DoctorReservationSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    address = serializers.SlugRelatedField(read_only=True, slug_field='zone')
    class Meta :       
        model = Reservation
        fields = ("patient" , "address" , "description" , "status") 

