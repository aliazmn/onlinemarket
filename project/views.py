from django.shortcuts import render

def test(request):
    return render(request,"Product/product_category.html",{})