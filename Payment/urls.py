from django.urls import path,include
from .views import go_to_gateway_view,callback_gateway_view

app_name="Payment"

urlpatterns = [
    path("go_to",go_to_gateway_view,name="gotogetway"),
    path("callback",callback_gateway_view,name="callback"),

]
