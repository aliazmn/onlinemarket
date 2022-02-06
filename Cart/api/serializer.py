
from rest_framework import serializers
from Cart.utils import add_cart_api

class CartSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=255)
    color = serializers.CharField(max_length = 255 , required=False)
    size = serializers.CharField(max_length = 255 , required=False)
    count = serializers.IntegerField()
    
    def __init__(self, request,instance=None, data=..., **kwargs):
        self.request = request
        super().__init__(instance, data, **kwargs)
    
    def create(self, validated_data ,name):
        if self.request.user.is_authenticated:
            add_cart_api(self.request,self.request.session.session_key)
        else:
            add_cart_api(self.request,self.request.user.email)
