from ast import Delete
from django.shortcuts import render , get_object_or_404
from rest_framework import generics , permissions , status
from .serializers import DepartmentSerializer ,PrivateDepartmentSerializer 
from doctor.serializers import DoctorSerializer
from .models import Department
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from knox.auth import TokenAuthentication
from knox.models import AuthToken 
from users.models import ExtendUser


#########################################  Create Department  ###################################

class CreateDepartment(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)    
    serializer_class = PrivateDepartmentSerializer
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
        serializer.save()
        return Response(
            { 
                "message": "Done"
            }
        )
    
#########################################  delete Department  ###################################

class DeleteDepartment(generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)    
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, department_id):
        department = Department.objects.get(pk=department_id)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            return Response(
            { 
                "message": "You don't have permission"
            }
            )             
        department.delete()
        return Response(
            { 
                "message": "Done"
            }
        )

        


#########################################  Get All Department  ###################################

class GetAll (APIView):
    def get(self, request):
        departments = Department.objects.all()
        data = DepartmentSerializer(departments, many=True).data
        return Response(data)

#########################################  Get one Department  ##################################    

@api_view(['GET'])
def get_department(request,department_id):
     department = get_object_or_404(Department,pk=department_id)
     data = DepartmentSerializer(department).data
     return Response (data)

#########################################  Update Department  ###################################

class UpdateDepartment(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PrivateDepartmentSerializer  
    permission_classes = (permissions.IsAuthenticated,)
          
    def update(self, request, department_id):
        self.object = Department.objects.get(pk=department_id)
        instance = self.object
        instance.name = request.data.get("name")
        instance.description = request.data.get("description")
        serializer = self.get_serializer(data = request.data)        
        is_superuser = request.user.is_superuser
        if not is_superuser:
            return Response(
            { 
                "message": "You don't have permission"
            }
            )
        serializer.is_valid(raise_exception=True) 
        instance.save()  
        return Response(
            { 
                'message': 'updated successfully'
            }
        )
 
    



