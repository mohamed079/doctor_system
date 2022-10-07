from asyncore import read
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers  , validators
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate
from .models import ExtendUser

############################################    ExtendUser Serializer ###############################################

class ExtendUserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = ExtendUser
        fields = ("first_name" , "last_name" , "username" , "email" , "gender" , "age" , "birth_date" , "phone_number" , 
        "image" , "is_superuser" , "is_staff")

############################################    Register Serializer  ###############################################

class RegisterSerializer(serializers.ModelSerializer):
    class Meta :
        model = ExtendUser
        fields = ("first_name" , "last_name" , "username" ,  "password"  , "email" , "gender" , "age" , "birth_date" , "phone_number" , 
        "image" , "is_superuser" , "is_staff") 
        extra_kwargs = {
            "passeord" : {"write_only" : True},
            "email" : {
                "required" : True ,
                "allow_blank" : False ,
                "validators" : [
                    validators.UniqueValidator(
                        ExtendUser.objects.all() , "A User With That Email Already Exists"
                    )
                ] 
            }
        }

    age = serializers.DecimalField(max_digits=3 , decimal_places=0 ,required = True)

    def check_phone(data):
      if len(data) < 11 :
         raise serializers.ValidationError('Phone Number is invalid')
      if len(data) > 11 :
         raise serializers.ValidationError('Phone Number is invalid')


    phone_number = serializers.CharField(required = True)
    phone_number = serializers.CharField(validators=[check_phone ,RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format '+123456789'") , validators.UniqueValidator( ExtendUser.objects.all() , "A User With That Phone Number Already Exists" )])

    def check_password(data):
     if len(data) < 8 :
        raise serializers.ValidationError('Password must be at least 8 characters')

    password = serializers.CharField(validators=[check_password])

    def create(self, validated_data ):
        user = ExtendUser.objects.create_user(
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
            username = validated_data["username"],
            password = validated_data["password"],
            email = validated_data["email"],
            gender = validated_data["gender"],
            age = validated_data["age"],
            birth_date = validated_data["birth_date"],
            phone_number = validated_data["phone_number"],
            image = validated_data["image"],
            is_superuser = validated_data ["is_superuser"],
            is_staff = validated_data ["is_staff"],
        )      
        return user

############################################    login Serializer  ###############################################

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
           raise serializers.ValidationError('A user with this Email and password is not found')

        return user

############################################   Change Password Serializer ###############################################

class ChangePasswordSerializer (serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def check_password(data):
     if len(data) < 8 :
        raise serializers.ValidationError('Password must be at least 8 characters')

    new_password = serializers.CharField(validators=[check_password])


