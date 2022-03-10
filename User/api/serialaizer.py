from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from User.utils import Send_email
from User.models import Customer,Address
from User.models import Profile

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



User = get_user_model()

#-------------------create jwt token----------------------
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['email'] = Profile.email
        return token


class LoginSerializer(serializers.Serializer):
    token = MyTokenObtainPairSerializer(many=True, read_only=True)
    email=serializers.EmailField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style= {'input_type':'password'},
        trim_whitespace=False,
        write_only=True
    )

class RegisterSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Profile.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    re_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email','address','postal_code','password', 're_password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'address': {'required': True},
            'postal_code': {'required': True},
            'password': {'required': True},
            're_password': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Profile.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            postal_code=validated_data['postal_code']
        )

        #----------- save user and activate false----------
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        #------------- set user address and create customer-----------
        cus=Customer.objects.create(profile=user)
        address=Address(add=validated_data['address'],postalcode=validated_data['postal_code'])
        address.save()
        cus.add.add(address)
        cus.save()  
        req =  self.context['request']
        opt="activate"
        to_email = validated_data['email']
        Send_email(req,to_email,opt) 

        return user

