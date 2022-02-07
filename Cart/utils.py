import json
from math import prod

from django.shortcuts import render,redirect,get_object_or_404
from django.core.cache import caches
from django.core import cache

from Product.models import Product



def set():
    redis_cache=caches['default']
    cart = redis_cache.client.get_client()
    return cart
    
    
def add_cart(request,name,detect = None):
    cart = set()
    if cart.hlen(name) > 0:
        keys = cart.hkeys(name)
        for elm in keys:
            if elm.decode("utf-8") == detect:
                same_product = cart.hget(name,detect)
                same_product = json.loads(same_product)
                same_product["count"] = int(same_product["count"]) + int(request.POST["count"])
                cart.hset(name,detect,json.dumps(same_product))
    else:             
        cart.hset(name,detect,json.dumps(request.POST))
    

def add_cart_api(valid_data,name):

    product = get_object_or_404(Product , pk = valid_data.get("id"))
    detect = product.name+valid_data.get("color","")+valid_data.get("size","")
    cart = set()
    dict_cart={
        "name":product.name,
        "id":product.id,
        "amount":product.amount,
        "price":product.price,
        "brand":product.brand,
        "color":valid_data.get("color"),
        "size":valid_data.get("size"),
        "count":valid_data.get("count"),
        "detect":detect
    }
    if cart.hlen(name) > 0:
        keys = cart.hkeys(name)
        for elm in keys:
            if elm.decode("utf-8") == detect:
                same_product = cart.hget(name,detect)
                same_product = json.loads(same_product)
                same_product["count"] = int(same_product["count"]) + int(dict_cart["count"])
                cart.hset(name,detect,json.dumps(same_product))
    else:       
        cart.hset(name,detect,json.dumps(dict_cart))



def show_cart_utils(request,name):
    cart = set()
    if not request.session.session_key:
        request.session.save()
    prod_list,ctx,price_totoal={},{},0
    # try:
    my_cart=cart.hgetall(name)

    for item in my_cart:
        elm = json.loads(my_cart[item])
        product = get_object_or_404(Product,id = elm.get("id"))
        if int(elm.get("count")) > int(product.amount):
            elm["status"] = False
        else:
            elm["status"]=True
            elm["price"] = int(product.price)*int(elm.get("count"))
            price_totoal+= elm["price"]
            elm["price_total"] = price_totoal
        prod_list[elm["name"]]=elm

    
    ctx["show"] = prod_list
    ctx["price_total"] = price_totoal
    return ctx
    # except:
    #     ctx ["show"]=""
    #     ctx["price_total"] = 0
        
    #     return ctx 