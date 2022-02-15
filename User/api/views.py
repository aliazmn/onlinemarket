
from django.contrib.auth import login as _login , authenticate,logout


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView


from urllib import response
from pytz import timezone


from User.models import Profile
from User.api.serialaizer import LoginSerializer,RegisterSerializer



#---------------------------------------------APIregister------------------------------
class RegisterView(generics.CreateAPIView):
 
    queryset = Profile.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


#--------------------------------------------APIlogin-----------------------------------
class Login_api(TokenObtainPairView):

    def post(self,request):
        serialaizer = LoginSerializer(data=request.data)
        
        if serialaizer.is_valid():
            email=serialaizer.validated_data["email"]
            password=serialaizer.validated_data["password"]
            user=authenticate(email=email,password=password)
            if user:
                _login(request,user)
                return Response(serialaizer.data,status=status.HTTP_202_ACCEPTED)
            else:
                return response(serialaizer.data,status=status.HTTP_404_NOT_FOUND)



@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def logout_api(request):
    logout(request)
    return Response('User Logged out successfully')