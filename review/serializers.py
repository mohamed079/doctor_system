from .models import Review
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    class Meta :       
        model = Review
        fields = ("rate" , "feedback") 
        
    def create(self, validated_data ):
        review = Review.objects.create(
            patient = validated_data["patient"],
            doctor = validated_data["doctor"],
            rate = validated_data["rate"],
            feedback = validated_data["feedback"],
        )      
        return review  

