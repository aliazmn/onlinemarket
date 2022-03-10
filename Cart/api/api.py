import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from Cart.utils import show_cart_utils
from .serializer import CartSerializer

class Cart(APIView):
    
    def get(self,request):

        if not request.user.is_authenticated:
            dict_cart = show_cart_utils(request,request.session.session_key)
        else:
            
            dict_cart = show_cart_utils(request,request.user.email)

        
        dict_cart = dict_cart["show"]
        dicc={}
        for key,value in dict_cart.items():
            dicc[key]={
     
                    "id":value["id"],
                    "name":value["name"],
                    "color":value.get("color",""),
                    "size":value.get("size",""),
                    "count":value["count"],
                    "price_total":value["price_total"],
                
            }
        return Response(dicc)  
    

    def post(self,request):

        serialized=CartSerializer(request,data=request.data)
        if serialized.is_valid():
            return serialized.create_cart()
            

        else:
            return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
    