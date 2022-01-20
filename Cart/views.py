import json
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.cache import caches
from Product.models import Product


def add_to_cart(request):
    redis_cache=caches['default']
    cart=redis_cache.client.get_client()
    if not request.session.session_key:
        request.session.save()
    detect=request.POST.get("name","")+request.POST.get("color","")+request.POST.get("سایزلباس","")

    if (int(request.POST.get("amount")) - int(request.POST.get("count"))) >= 0:


        if not request.user.is_authenticated:
            if cart.hlen(request.session.session_key) > 0:
                keys=cart.hkeys(request.session.session_key)
                for elm in keys:
                    if elm.decode("utf-8")==detect:
                        s=cart.hget(request.session.session_key,detect)
                        s=json.loads(s)
                        s["count"]=int(s["count"])+int(request.POST["count"])
                        cart.hset(request.session.session_key,detect,json.dumps(s))

            else:
                
                cart.hset(request.session.session_key,detect,json.dumps(request.POST))

            return redirect("product:detailproduct",request.POST.get("id"))

        else:
            if cart.hlen(request.user.email) > 0:
                keys=cart.hkeys(request.user.email)
                for elm in keys:
                    if elm.decode("utf-8")==detect:
                        s=cart.hget(request.user.email,detect)
                        s=json.loads(s)
                        s["count"]=int(s["count"])+int(request.POST["count"])
                        cart.hset(request.user.email,detect,json.dumps(s))
            else:
                cart.hset(request.user.email,detect,json.dumps(request.POST))
            return redirect("product:detailproduct",request.POST.get("id"))

    else:
        return HttpResponse("tedad kafi nist ")

def show_cart(request):
    redis_cache=caches['default']
    cart=redis_cache.client.get_client()
    if not request.session.session_key:
            request.session.save()

    if not request.user.is_authenticated:

        my_cart=cart.hgetall(request.session.session_key)
        value=[]
        for elm in my_cart:
            value.append(json.loads(my_cart[elm]))
        
        prod_list,ctx,price_totoal=[],{},0
        for elm in value:
            elm["price"]=int(elm.get("price"))*int(elm.get("count"))
            price_totoal+=elm["price"]
            elm["price_total"]=price_totoal
            elm["detect"]=elm.get("name","")+elm.get("color","")+elm.get("سایزلباس","")
            prod_list.append(elm)

        ctx["show"]=prod_list
        ctx["price_total"]=price_totoal
        


        return render(request,"Cart/cart.html",ctx)
    
    else:


        my_cart=cart.hgetall(request.user.email)
        value=[]
        for elm in my_cart:
            value.append(json.loads(my_cart[elm]))
        
        prod_list,ctx,price_totoal=[],{},0
        for elm in value:
            elm["price"]=int(elm.get("price"))*int(elm.get("count"))
            price_totoal+=elm["price"]
            elm["price_total"]=price_totoal
            elm["detect"]=elm.get("name","")+elm.get("color","")+elm.get("سایزلباس","")
            prod_list.append(elm)

        ctx["show"]=prod_list
        ctx["price_total"]=price_totoal
        


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
