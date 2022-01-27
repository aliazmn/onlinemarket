import json

from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
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
                        same_product=cart.hget(request.session.session_key,detect)
                        same_product=json.loads(same_product)
                        same_product["count"]=int(same_product["count"])+int(request.POST["count"])
                        cart.hset(request.session.session_key,detect,json.dumps(same_product))
            else:             
                cart.hset(request.session.session_key,detect,json.dumps(request.POST))
            return redirect("product:detailproduct",request.POST.get("id"))
        else:
            if cart.hlen(request.user.email) > 0:
                keys=cart.hkeys(request.user.email)
                for elm in keys:
                    if elm.decode("utf-8")==detect:
                        same_product=cart.hget(request.user.email,detect)
                        same_product=json.loads(same_product)
                        same_product["count"]=int(same_product["count"])+int(request.POST["count"])
                        cart.hset(request.user.email,detect,json.dumps(same_product))
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
            product = get_object_or_404(Product,name = elm.get("name"))
            if int(elm.get("count")) > int(product.amount):
                elm["status"] = False
            else:
                elm["status"]=True
                elm["price"] = int(product.price)*int(elm.get("count"))
                price_totoal+= elm["price"]
                elm["price_total"] = price_totoal
            elm["detect"] = elm.get("name","")+elm.get("color","")+elm.get("سایزلباس","")
            prod_list.append(elm)
        ctx["show"] = prod_list
        ctx["price_total"] = price_totoal
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









# @require_POST
# def cart_add(request,product_id):
#     cart=Cart(request)
#     product=get_object_or_404(Product,id=product_id)
#     form=CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd=form.clean_data
#         cart.add(product=product,quantity=cd['quantity'],override_quantity=cd['override_quantity'])
#     return redirect ('cart:cart_detail')


# def cart_remove(request,product_id):
#     cart=Cart(request)
#     product=get_object_or_404(Product,id=product_id)
#     cart.remove(product)
#     return redirect ('cart:cart_detail')

# def cart_detail(request):
#     cart=Cart(request)
#     return redirect ('cart/detail.html',{'cart':cart})
    







