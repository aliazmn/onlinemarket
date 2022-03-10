from django.shortcuts import redirect
from rest_framework import serializers
from Cart.utils import add_cart_api


class CartSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    color = serializers.CharField(max_length = 255 , required=False ,allow_blank = True)
    size = serializers.CharField(max_length = 255 , required=False ,allow_blank = True )
    count = serializers.IntegerField()
    # cart_dict= serializers.DictField()
    
    def __init__(self, request,instance=None, data=..., **kwargs):
        self.request = request
        super().__init__(instance, data, **kwargs)
    
    
    def create_cart(self):

        if not self.request.user.is_authenticated:
            add_cart_api(self.validated_data,self.request.session.session_key)
        else:
            add_cart_api(self.validated_data,self.request.user.email)

        return redirect("cart:show-cart-api")
