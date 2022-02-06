import json

from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.cache import caches

from Product.models import Product
from .utils import add_cart,show_cart_utils

def add_to_cart(request):
    detect = request.POST.get("name","")+request.POST.get("color","")+request.POST.get("سایزلباس","")
    if (int(request.POST.get("amount")) - int(request.POST.get("count"))) >= 0:
        if not request.user.is_authenticated:
            if not request.session.session_key:
                request.session.save()
            add_cart(request,request.session.session_key,detect)
            return redirect("product:detailproduct",request.POST.get("id"))
        else:
            add_cart(request,request.user.email,detect)
            return redirect("product:detailproduct",request.POST.get("id"))

    else:
        return HttpResponse("tedad kafi nist ")


def show_cart(request):

    if not request.user.is_authenticated:
        if not request.session.session_key:
            request.session.save()
        ctx=show_cart_utils(request,request.session.session_key)
        return render(request,"Cart/cart.html",ctx)
        
    else:
        ctx=show_cart_utils(request,request.user.email)
        return render(request,"Cart/cart.html",ctx)



def delete_cart(request,detail):
    redis_cache=caches['default']
    cart=redis_cache.client.get_client()
    if not request.user.is_authenticated:
        cart.hdel(request.session.session_key,detail)
        return redirect("cart:show-cart")
    else:
        cart.hdel(request.user.email,detail)
        return redirect("cart:show-cart")








