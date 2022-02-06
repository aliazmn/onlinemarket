
from itertools import product
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from Product.models import Product,Category
from project.Api.serializers import CategorySerializer
from Product.Api.serializers import ProductDetailSerializer, ProductListSerializer


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        query=Category.objects.all().filter(sub_cat=None).order_by('cat_title')
        serializer_class = CategorySerializer(query ,many=True)
        return Response(serializer_class.data)



# class ProductListViewset(viewsets.ViewSet):
   
#     def list(self, request):
       
#         queryset = Product.objects.all().order_by('date_create')
#         serializer = ProductListSerializer(queryset,context={'request':request}, many=True)
#         return Response(serializer.data)



class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    

    






