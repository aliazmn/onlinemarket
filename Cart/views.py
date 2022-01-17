from contextlib import redirect_stdout
from itertools import product
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from Cart.models import CartItem, CartMe
from Product.models import Product
from django.views.decorators.http import require_POST


@require_POST
def add_to_cart(request):
    if request.user.is_authenticated:
        user=request.user
        count = int(request.POST.get('count'))
        cart_me=CartMe.objects.get_or_create(user_id=request.user.id, is_paid=False) 
        product = get_object_or_404(Product, name=request.POST.get("name"))
        cart_item = CartItem.objects.create(cart=user,product=request.POST.get("name"))
        if product.amount - count < 0 :
            raise ValueError("product not exist")
        else:
            cart_item.save()
            cart_me.add.cart(CartItem)
            cart_item.save()

    else:
        pass


            





