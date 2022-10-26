from gc import get_objects
from multiprocessing.spawn import import_main_path
from django.shortcuts import render , get_object_or_404
from rest_framework import generics , permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.auth import TokenAuthentication
from .models import Address
from .serializers import PatientAddressSerializer , DoctorAddressSerializer ,GeneralDoctorAddressSerializer

############################################    create patient address   ###############################################

class CreatePatientAddress (generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)    
    serializer_class = PatientAddressSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post (self , request , *args , **kwargs):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user=request.user)
        return Response (
            {
              'message': 'Done'
            }
        )

############################################    create doctor address   ###############################################

class CreateDoctorAddress (generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)    
    serializer_class = DoctorAddressSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post (self , request , *args , **kwargs):        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user=request.user)
        return Response (
            {
              'message': 'Done'
            }
        )


#########################################  delete Address  ###################################

class DeleteAddress(generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)    
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request , address_id):
        address = Address.objects.get(pk=address_id)
        address.delete()
        return Response(
            { 
                "message": "Done"
            }
        )

#########################################  Update Patient Address  ###################################

class UpdatePatientAddress(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PatientAddressSerializer  
    permission_classes = (permissions.IsAuthenticated,)
          
    def update(self, request , address_id):
        self.object = Address.objects.get(pk = address_id)
        instance = self.object
        instance.city = request.data.get("city")
        instance.zone = request.data.get("zone")
        instance.street_name = request.data.get("street_name")
        instance.building_number = request.data.get("building_number")
        instance.flat_number = request.data.get("flat_number")
        instance.land_mark = request.data.get("land_mark")
        serializer = self.get_serializer(data = request.data)        
        serializer.is_valid(raise_exception=True) 
        instance.save()  
        return Response(
            { 
                'message': 'updated successfully'
            }
        )
#########################################  Update doctor Address  ###################################

class UpdateDoctorAddress(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = DoctorAddressSerializer  
    permission_classes = (permissions.IsAuthenticated,)
          
    def update(self, request , address_id):
        self.object = Address.objects.get(pk = address_id)
        instance = self.object
        instance.city = request.data.get("city")
        instance.zone = request.data.get("zone")
        instance.street_name = request.data.get("street_name")
        instance.building_number = request.data.get("building_number")
        instance.flat_number = request.data.get("flat_number")
        instance.land_mark = request.data.get("land_mark")
        instance.days = request.data.get("days")
        instance.start_time = request.data.get("start_time")
        instance.end_time = request.data.get("end_time")
        serializer = self.get_serializer(data = request.data)        
        serializer.is_valid(raise_exception=True) 
        instance.save()  
        return Response(
            { 
                'message': 'updated successfully'
            }
        )

#########################################  Get All Address of patient  ###################################

class GetPatientAddress (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PatientAddressSerializer  
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        address = Address.objects.filter(user=request.user)
        data = self.get_serializer(address, many=True).data
        return Response(data)

#########################################  Get All Address of doctor  ###################################

class GetDoctorAddress (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = GeneralDoctorAddressSerializer  
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        address = Address.objects.filter(user=request.user)
        data = self.get_serializer(address, many=True).data
        return Response(data)