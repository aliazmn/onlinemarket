
from django.urls import path

from Product.Api.Product_api import  ProductDetailView, ProductListView,CategoryDetailView
from .views import ProductDetail, Show_wishList,ShowProduct, add_to_wishlist, delete_from_wishlist

app_name="Product"
urlpatterns = [
    path('detailproduct/<int:product_id>',ProductDetail.as_view(),name="detailproduct"),
    path('show-product-by-category/',ShowProduct.as_view(),name="showproduct"),
    path("add-wishlist/", add_to_wishlist, name="add_wishlist"),
    path("del-wishlist/<int:id>", delete_from_wishlist, name="delete_wishlist"),
    path("show-wishlist/", Show_wishList.as_view(), name="Show_wishList"),

   #API PATH
  
    path('apiproduct-list/', ProductListView.as_view(), name='product_list'),
    path('apiproduct-detail/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('categorydetail/<int:pk>',CategoryDetailView.as_view(),name='category_detail'),
]


