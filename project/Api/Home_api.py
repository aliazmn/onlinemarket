
from itertools import product
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from Product.Api.serializers import ProductListSerializer


from Product.models import Product,Category
from project.Api.serializers import CategorySerializer





class SearchProductList(viewsets.ViewSet):
     def list(self, request):
        query =request.GET.get('search')
        queryset = Product.objects.filter(name__icontains=query)
        serializer_class = ProductListSerializer(queryset,context={'request':request}, many=True)
      
        return Response(serializer_class.data)

