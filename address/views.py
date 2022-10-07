from gc import get_objects
from multiprocessing.spawn import import_main_path
from django.shortcuts import render
from rest_framework import generics , permissions , status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from .models import Address
from users.models import ExtendUser
from .serializers import AddressSerializer
from rest_framework.authtoken.models import Token
from rest_framework import response

############################################    create address   ###############################################

class CreateAddress (generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)    
    serializer_class = AddressSerializer
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

    def delete(self, request):
        address = Address.objects.get(user=request.user)
        address.delete()
        return Response(
            { 
                "message": "Done"
            }
        )

#########################################  Update Address  ###################################

class UpdateAddress(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = AddressSerializer  
    permission_classes = (permissions.IsAuthenticated,)
          
    def update(self, request):
        self.object = Address.objects.get(user = request.user)
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

#########################################  Get All Address of user  ###################################

class Get (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = AddressSerializer  
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        address = Address.objects.filter(user=request.user)
        data = self.get_serializer(address, many=True).data
        return Response(data)

