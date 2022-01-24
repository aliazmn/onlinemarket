
from django.urls import path


from .views import ProductDetail, Show_wishList,ShowProduct,Filtering, add_to_wishlist, delete_from_wishlist

app_name="Product"
urlpatterns = [
    path('detailproduct/<int:product_id>',ProductDetail.as_view(),name="detailproduct"),
    path('show-product-by-category/',ShowProduct.as_view(),name="showproduct"),
    path('product-filter/',Filtering.as_view(),name="filter"),
    path("show-wishlist/<int:id>", Show_wishList.as_view(), name="Show_wishList"),
    path("add-wishlist/", add_to_wishlist, name="add_wishlist"),
    path("delete-wishlist/", delete_from_wishlist, name="delete_wishlist"),


    


]

