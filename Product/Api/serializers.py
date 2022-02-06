

from rest_framework import serializers
from Comment.Api.serializers import CommentSerializer
from Product.models import Product,Category


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Product
        fields = ['url','name','img','brand','price']
        extra_kwargs = {
        'url': {'view_name': 'product:product_detail', 'lookup_field': 'slug'}
        }
    




class ProductDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 
                  'price','img','img1','img2','cat_id','comments']  





class CategorySerializer(serializers.HyperlinkedModelSerializer):
    
    cattocat = serializers.StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ['cat_title','cattocat']

