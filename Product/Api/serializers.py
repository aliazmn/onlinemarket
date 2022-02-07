

from itertools import product
from pickle import TRUE
from pyexpat import model
from unicodedata import category
from attr import field
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
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 
                  'price','img','img1','img2','cat_id','comments']  




class RelatedCategorySerializer(serializers.ModelSerializer):
    producttocat=ProductListSerializer(many=True)
    class Meta:
        model=Category
        fields=['cat_title','producttocat']
        # extra_kwargs={
        #     'url' :{'view_name':'product:product_list'}
        # }


class CategoryDetailSerializer(serializers.ModelSerializer):
    cattocat=RelatedCategorySerializer(many=True)

    class Meta:
        model=Category
        fields = ['cattocat']
        
       


class CategoryListgSerializer(serializers.HyperlinkedModelSerializer):
    cattocat=serializers.StringRelatedField(many=True)
   

    class Meta:
        model = Category
        fields = ['url','cat_title','cattocat',]
        extra_kwargs = {
        'url': {'view_name': 'product:category_detail', 'lookup_field':'pk'}
        }
      

