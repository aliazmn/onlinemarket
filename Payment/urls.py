from django.urls import path
from .views import payment_start,payment_return,show_factors

app_name="Payment"
urlpatterns = [

    path('payment-start/<int:amount>', payment_start, name="payment_start"),
    path('payment-return/', payment_return, name="payment_return"),
    path("showfactor",show_factors,name="showfactor"),
]
