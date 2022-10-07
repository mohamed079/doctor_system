import email
from logging import raiseExceptions
from multiprocessing import context
from django.shortcuts import render
from patient.models import Patient
from .models import Doctor
from users.models import ExtendUser
from .serializers import DoctorSerializer , RegisterSerializer  , LoginSerializer , ChangePasswordSerializer
from rest_framework import generics , permissions , status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from knox.models import AuthToken 
from users.serializers import ExtendUserSerializer 


############################################    Register API   ###############################################

class RegisterAPI (generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post (self , request , *args , **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception = True)
        user = serializers.save()
        return Response (
            {
                'message': 'Doctor Registration Successful! Please Login.'
            }
        )

############################################    Login API   ###############################################

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post (self , request , *args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        patient = Patient.objects.filter(email=user.email)
        if patient:
          return Response(
            { 
                'message': 'Wrong Credentials',
            }
        )
        doctor = Doctor.objects.get(email=user.email)
        return Response(
            { 
                "user" : DoctorSerializer(doctor , context = self.get_serializer_context(),).data,
                "token":AuthToken.objects.create(user)[1],
            }
        )


############################################   Change Password API   ###############################################

class ChangePasswordAPI(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ChangePasswordSerializer
    model = ExtendUser
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'message': 'Password updated successfully',
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


############################################    get doctor Serializer  ###############################################

class UserAPI (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = DoctorSerializer 

    def get_object (self):
        doctor = Doctor.objects.get(email=self.request.user.email)
        return doctor

############################################    Get All doctor Serializer  ###############################################

class GetAll (APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        data = DoctorSerializer(doctors, many=True).data
        return Response(data)        
