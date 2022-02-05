import json
from math import prod

from django.shortcuts import render,redirect,get_object_or_404
from django.core.cache import caches


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
                same_product = cart.hget(request.session.session_key,detect)
                same_product = json.loads(same_product)
                same_product["count"] = int(same_product["count"]) + int(request.POST["count"])
                cart.hset(name,detect,json.dumps(same_product))
    else:             
        cart.hset(name,detect,json.dumps(request.POST))
    

def add_cart_api(request,name):
    product = get_object_or_404(Product , pk = request.data.get("product_id"))
    detect = product.name+request.data.get("color","")+request.data.get("size","")
    cart = set()
    dict_cart={
        "name":product.name,
        "id":product.id,
        "img":product.img,
        "amount":product.amount,
        "price":product.price,
        "brand":product.brand,
        "color":request.data.get("color"),
        "size":request.data.get("size"),
        "count":request.data.get("count"),
        "detect":detect
    }
    if cart.hlen(name) > 0: 
        pass
    
    else:
        cart.hset(name,detect,json.dumps(dict_cart))



def show_cart_utils(request,name):
    cart = set()
    my_cart=cart.hgetall(name)
    prod_list,ctx,price_totoal=[],{},0
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
        elm.setdefault("detect" ,elm.get("name","")+elm.get("color","")+elm.get("سایزلباس",""))
        prod_list.append(elm)


    ctx["show"] = prod_list
    ctx["price_total"] = price_totoal
    return ctx
