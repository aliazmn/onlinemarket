from django.urls import path
from .views import add_to_cart,show_cart,delete_cart

app_name="Cart"
urlpatterns = [
    path("add-to-cart",add_to_cart,name="add-to-cart"),
    path("show-cart",show_cart,name="show-cart"),
    path("delete-cart/<str:detail>",delete_cart,name="delete-cart"),


]
