from gc import get_objects
from multiprocessing.spawn import import_main_path
from django.shortcuts import render , get_object_or_404
from rest_framework import generics , permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.auth import TokenAuthentication
from .models import Address
from .serializers import PatientAddressSerializer , DoctorAddressSerializer ,GeneralDoctorAddressSerializer
from rest_framework.decorators import APIView
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

class UpdatePatientAddress(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def patch (self, request , address_id):
        instance= Address.objects.get(pk = address_id , user=self.request.user.id)
        serializer = PatientAddressSerializer(instance , data=request.data , partial = True )        
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(serializer.data)          

#########################################  Update doctor Address  ###################################

class UpdateDoctorAddress(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
          
    def patch (self, request , address_id):
        instance= Address.objects.get(pk = address_id , user=self.request.user.id)
        serializer = DoctorAddressSerializer(instance , data=request.data , partial = True )        
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(serializer.data)          

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