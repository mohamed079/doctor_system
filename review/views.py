from rest_framework import generics , permissions , status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from .serializers import ReviewSerializer
from .models import Review
from doctor.models import Doctor
############################################    create Review   ###############################################

class CreateReview (generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)    
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post (self , request , doctor_id):
        doctor = Doctor.objects.get(pk = doctor_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(patient=request.user , doctor=doctor)
        return Response (
            {
              'message': 'Done'
            }
        )

#########################################  delete Review  ###################################

class DeleteReview(generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)    
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request , id_review):
        review = Review.objects.get(pk = id_review , patient=request.user)
        review.delete()
        return Response(
            { 
                "message": "Done"
            }
        )

#########################################  Update Review  ###################################

class UpdateReview(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ReviewSerializer  
    permission_classes = (permissions.IsAuthenticated,)
          
    def update(self, request , id_review):
        self.object = Review.objects.get(pk = id_review , patient=request.user)
        instance = self.object
        instance.rate = request.data.get("rate")
        instance.feedback = request.data.get("feedback")
        serializer = self.get_serializer(data = request.data)        
        serializer.is_valid(raise_exception=True) 
        instance.save()  
        return Response(
            { 
                'message': 'updated successfully'
            }
        )

#########################################  Get All Review of doctor  ###################################

class Get (APIView):
    def get(self, request , doctor_id):
        review = Review.objects.filter(pk = doctor_id)
        data = ReviewSerializer(review, many=True).data
        return Response(data)

