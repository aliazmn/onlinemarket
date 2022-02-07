import json

from Product.models import Product
from django.shortcuts import get_object_or_404
from Cart.models import History
from django.core.cache import caches

def create_factor(request,bankrecord):
    history=History()
    print(request.user)
    history.customer=request.user
    redis_cache=caches['default']
    cart=redis_cache.client.get_client()
    my_cart=cart.hgetall(request.user.email)
    value,counter={},1
    for elm in my_cart:
        value[f"product{counter}"]=json.loads(my_cart[elm])
    for i in value:
        product=get_object_or_404(Product,id=value[i].get("id"))
        product.amount = product.amount - int(value[i].get("count"))
        product.save()
        value[i].pop("csrfmiddlewaretoken")
        value[i].pop("id")
        value[i].pop("img")
        value[i].pop("amount")
        value[i].setdefault("tracingcode", bankrecord)
        counter+=1
        cart.hdel(request.user.email,elm)
    
    history.factor=value
    history.save()