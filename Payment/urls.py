from django.urls import path,include
from .views import go_to_gateway_view,callback_gateway_view,show_factors

app_name="Payment"

urlpatterns = [
    path("go_to/<int:price_total>",go_to_gateway_view,name="gotogetway"),
    path("callback",callback_gateway_view,name="callback"),
    path("showfactor",show_factors,name="showfactor"),
    

]
