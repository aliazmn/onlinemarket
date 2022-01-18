
from django.contrib import admin
from django.urls import path

from django.urls import path

from .views import ProductDetail,ShowProduct,Filtering, add_to_wishlist

app_name="Product"
urlpatterns = [
    path('detailproduct/<int:product_id>',ProductDetail.as_view(),name="detailproduct"),
    path('show-product-by-category/',ShowProduct.as_view(),name="showproduct"),
    path('product-filter/',Filtering.as_view(),name="filter"),
    path("add-wishlist/", add_to_wishlist, name="add_wishlist"),
    # path("test/", test, name="test"),

    


]

