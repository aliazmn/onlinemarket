
from cgitb import lookup
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
import django_filters.rest_framework
from Product.Api.filter import ProductFilterSet
from rest_framework.filters import SearchFilter
from Product.models import Product,Category
from Product.Api.serializers import  CategoryDetailSerializer, CategoryListgSerializer, ProductDetailSerializer, ProductListSerializer


class CategoryListViewSet(viewsets.ViewSet):
    def list(self, request):
        query=Category.objects.all().filter(sub_cat=None).order_by('cat_title')
        serializer_class =  CategoryListgSerializer(query ,context={'request':request},many=True)
        return Response(serializer_class.data)


class CategoryDetailView(RetrieveAPIView):

    queryset=Category.objects.filter(sub_cat=None).order_by('cat_title')
    serializer_class= CategoryDetailSerializer
    lookup_field='pk'




class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilterSet
    search_fields = ['name','brand']


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    


