from django.shortcuts import render
from rest_framework import generics , permissions
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from .serializers import  ReservationSerializer , PatientReservationSerializer , DoctorReservationSerializer 
from .models import Reservation
from address.models import Address
from doctor.models import Doctor

############################################    create Reservation   ###############################################

class CreateReservation (generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)    
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post (self , request ,id_address , id_doctor):
        address = Address.objects.get(pk = id_address)
        doctor = Doctor.objects.get(pk = id_doctor)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(patient=request.user ,doctor=doctor , address = address)
        return Response (
            {
              'message': 'Done'
            }
        )

#########################################  Get All Reservation of patient  ###################################

class GetPatientReservation (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PatientReservationSerializer  
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        reservation = Reservation.objects.filter(patient=request.user)
        data = self.get_serializer(reservation, many=True).data
        return Response(data)

########################################  Get All appointment of doctor  ###################################

class GetDoctorReservation (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class =   DoctorReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        reservation = Reservation.objects.filter(doctor=request.user)
        data = self.get_serializer(reservation, many=True).data
        return Response(data)

########################################  manage appointment doctor  ###################################

class ManageDoctorReservation (generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class =   DoctorReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request , id_reservation):
        self.object = Reservation.objects.get(pk=id_reservation , doctor=request.user)
        instance = self.object
        instance.status = request.data.get("status")
        serializer = self.get_serializer(data = request.data)        
        serializer.is_valid(raise_exception=True) 
        instance.save()
        return Response(
            {                   
              'message': 'Done'
            }
        )

########################################  delete Reservation of patient  ###################################

class DeletePatientReservation(generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)    
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request , id_reservation):
        reservation = Reservation.objects.get(pk=id_reservation , patient=request.user)
        reservation.delete()
        return Response(
            { 
                "message": "Done"
            }
        )
