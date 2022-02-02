
import profile
from django.db import IntegrityError
from django.forms import ValidationError
from django.utils import timezone
from urllib import response
from venv import create
import django
from django.shortcuts import get_object_or_404
from pytz import timezone
from rest_framework import viewsets,status
from User.api.serialaizer import LoginSerializer,RegistrationSerializer
from User.models import Profile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login as _login , authenticate,logout
from rest_framework.authtoken.models import Token
from django.conf import settings 





@api_view(["POST"])
def login_api(request):
    serialaizer = LoginSerializer(data=request.data)
    result={}
    if serialaizer.is_valid():
        email=serialaizer.validated_data["email"]
        password=serialaizer.validated_data["password"]
        user=authenticate(email=email,password=password)
        token,created=Token.objects.get_or_create(user=user)
        if user:
            token,created=Token.objects.get_or_create(user=user)
            if settings.MY_USER_TOKEN_VALIDATION_DAY and isinstance(settings.MY_USER_TOKEN_VALIDATION_DAY):
                now=timezone.now()
                diffrence = now - token.created
                if diffrence.days > settings.MY_USER_TOKEN_VALIDATION_DAY:
                    token.delete()
                    token=Token.objects.create(user=user)
            # _login(request,user)
            result["sucssesful"]=True
            result["error"]=False
            result["data"]={"status":"login shodid","token":token.key}
            return Response(result)
        else:
            result["sucssesful"]=False
            result["error"]=True
            result["error_massage"]="email ya password eshtebah ast"
            return Response(result,status=status.HTTP_404_NOT_FOUND)
    else:
        result["sucssesful"]=False
        result["error"]=True
        result["error_massage"]=serialaizer.errors
        return response(result,status=status.HTTP_404_NOT_FOUND)



@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def logout_api(request):

    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')

 


@api_view(["POST"])
# @permission_classes([AllowAny])
def Register_api(request):
    result={}

    try:
        data = []
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            profile = serializer.save()
            profile.is_active = True
            profile.save()
            token = Token.objects.get_or_create(user=profile)[0].key
            data["message"] = "user registered successfully"
            data["email"] = profile.email
            data["first_name"] = profile.first_name
            data["last_name"] = profile.last_name
            data["postal_code"] = profile.postal_code
            data["address"] = profile.address
            data["token"] = token

        else:
            # data = serializer.errors
            result["sucssesful"]=False
            result["error"]=True
            result["error_massage"]=serializer.errors
            return response(result,status=status.HTTP_404_NOT_FOUND)

        return Response(data)

    except:
        profile=Profile.objects.get(username='')
        profile.delete()
        result["sucssesful"]=False
        result["error"]=True
        result["error_massage"]=serializer.errors
        return response(result,status=status.HTTP_404_NOT_FOUND)
















    # except IntegrityError as e:
    #     profile=Profile.objects.get(username='')
    #     profile.delete()
    #     raise ValidationError({"400": f'{str(e)}'})















# @api_view(["POST"])
# def logout_api(request):
#     serialaizer = LoginSerializer(request.data)
#     result={}
#     if serialaizer.is_valid():
#         email=serialaizer.validated_data["email"]
#         password=serialaizer.validated_data["password"]
#         user=authenticate(email=email,password=password)
#         token,created=Token.objects.get_or_create(user=user)

#         if settings.MY_USER_TOKEN_VALIDATION_DAY:
#             now=timezone.now()
#             diffrence = now - token.created
#             if diffrence.day > settings.MY_USER_TOKEN_VALIDATION_DAY:
#                 token.delete()
#                 return response({"status","login expired "})
#         if user:
#             # _login(request,user)
#             result["sucssesful"]=True
#             result["error"]=False
#             result["data"]={"status":"login shodid","token":user.email}
#             return Response(result)
#         else:
#             result["sucssesful"]=False
#             result["error"]=True
#             result["error_massage"]="email ya password eshtebah ast"
#             return Response(result,status=status.HTTP_404_NOT_FOUND)










# class LoginViewSet(viewsets.ModelViewSet):
#     serializer_class = LoginSerializer
#     queryset = Profile.objects.all()

#     @action(detail=True, methods=['post'])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
#         serializer = PasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_password(serializer.validated_data['password'])
#             user.save()
#             return Response({'status': 'password set'})
#         else:
            # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)