import email
from django.shortcuts import render
from rest_framework import generics , permissions , status
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from rest_framework.views import APIView
from doctor.models import Doctor
from patient.models import Patient
from users.models import ExtendUser
from .serializers import ExtendUserSerializer , RegisterSerializer  , LoginSerializer , ChangePasswordSerializer


############################################    Register API   ###############################################

class RegisterAPI (generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = RegisterSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post (self , request , *args , **kwargs):
        serializer = self.get_serializer(data=request.data)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            return Response(
            { 
                "message": "You don't have permission"
            }
            )
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response(
            { 
                "user" : ExtendUserSerializer(user , context = self.get_serializer_context(),).data,            
                'message': 'Registration Successful!'
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
        if doctor :
          return Response(
            { 
                'message': 'Wrong Credentials',
            }
        )
        patient = Patient.objects.filter(email=user.email)
        if patient :
          return Response(
            { 
                'message': 'Wrong Credentials',
            }
        )
        return Response(
            { 
                "user" : ExtendUserSerializer(user , context = self.get_serializer_context(),).data,            
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


############################################    get ExtendUser Serializer  ###############################################

class UserAPI (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ExtendUserSerializer 

    def get_object (self,request):
       user = self.request.user
       return user

############################################    Get All ExtendUser Serializer  ###############################################

class GetAll (APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = ExtendUserSerializer 

    def get(self, request):
        extend_user = ExtendUser.objects.filter(is_superuser =True )
        data = ExtendUserSerializer(extend_user, many=True).data
        is_superuser = request.user.is_superuser
        if not is_superuser:
            return Response(
            { 
                "message": "You don't have permission"
            }
            )

        return Response(data)        
