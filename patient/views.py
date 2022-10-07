from django.shortcuts import render
from doctor.models import Doctor
from .models import Patient
from users.models import ExtendUser
from .serializers import PatientSerializer , RegisterSerializer  , LoginSerializer , ChangePasswordSerializer
from rest_framework import generics , permissions , status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from knox.models import AuthToken 


############################################    Register API   ###############################################

class RegisterAPI (generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post (self , request , *args , **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception = True)
        user = serializers.save()
        return Response (
            {     
                'message': 'User Registration Successful! Please Login.'
            }
        )

############################################    Login API   ###############################################

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post (self , request , *args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        doctor = Doctor.objects.filter(email=user.email)
        if doctor:
          return Response(
            { 
                'message': 'Wrong Credentials',
            }
        )
        return Response(
            { 
                "user" : PatientSerializer(user , context = self.get_serializer_context(),).data,
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


############################################    get patient Serializer  ###############################################

class UserAPI (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = PatientSerializer 

    def get_object (self):

        patient = Patient.objects.get(email=self.request.user.email)
        return patient

############################################    Get All patient Serializer  ###############################################

class GetAll (APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        patients = Patient.objects.all()
        data = PatientSerializer(patients, many=True).data
        is_superuser = request.user.is_superuser
        if not is_superuser:
            return Response(
            { 
                "message": "You don't have permission"
            }
            )
        return Response(data)        
