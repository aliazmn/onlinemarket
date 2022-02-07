
from django.shortcuts import render
from django.views.generic import View, ListView

from Product.models import Category, Product


class Home(ListView):

    def get(self,request):
      
        newproduct=Product.objects.all().order_by('date_create')[:8]
        product=Product.objects.all().order_by('date_create')[8:22]
        context = { 
            'new_products':newproduct,
            'product':product
        }
        
        return render(request , 'home.html' ,context)


def searchbox(request):

    query =request.GET.get('search')
    if query:
        postresult = Product.objects.filter(name__icontains=query)
        result = postresult
    else:
        result = None
    conetxt={
        'result':result,
        } 
    return render(request ,'Product/product_category_name.html', conetxt)


       




