from django.urls import path

from Cart.views import add_to_cart, delete_cart, show_cart
from Cart.api.api import Cart

app_name="Cart"

urlpatterns = [
    path("add-to-cart",add_to_cart,name="add-to-cart"),
    path("show-cart",show_cart,name="show-cart"),
    path("delete-cart/<str:detect>",delete_cart,name="delete-cart"),
    
    path("api-cart",Cart.as_view() ,name="show-cart-api"),
    
   


]
