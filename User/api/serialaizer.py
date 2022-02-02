
import email
import profile
from django.utils import _os
from attr import fields
from django.forms import PasswordInput
from rest_framework import serializers
from User.models import Profile
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _




User = get_user_model()



class LoginSerializer(serializers.Serializer):
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
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )





class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "email",
            "postal_code",
            "address",
            "password",
            "re_password",

        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        profile = Profile(
        email=validated_data['email'],
        )
        password = validated_data["password"]
        re_password = validated_data["re_password"]
        if password == re_password:
            profile.set_password(password)
            profile.save()
        else:
            pass