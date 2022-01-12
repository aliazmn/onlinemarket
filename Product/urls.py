
from django.contrib import admin
from django.urls import path

from Product.views import category



urlpatterns = [
    path('category/', category ,name='category'),
]
