from rest_framework import generics , permissions , status
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from .serializers import ReviewSerializer
from .models import Review

############################################    create Review   ###############################################

class CreateReview (generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)    
    serializer_class = ReviewSerializer
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

#########################################  delete Review  ###################################

class DeleteReview(generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)    
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        review = Review.objects.get(user=request.user)
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
          
    def update(self, request):
        self.object = Review.objects.get(user = request.user)
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

#########################################  Get All Address of user  ###################################

class Get (generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ReviewSerializer  
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        review = Review.objects.filter(user=request.user)
        data = self.get_serializer(review, many=True).data
        return Response(data)

