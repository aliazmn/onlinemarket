from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from Comment.forms import CommentForm
from Comment.models import CommentMe

from Product.models import Product
# Create your views here.
def detail(request):
    return render(request , 'Products/product_details.html')


@login_required(login_url="")
def add_comment(request, product_id):
    if request.method=="GET":
        comments=CommentMe.objects.all().filter(product=product_id)

        context = {
            'form': CommentForm(),
            'comment':comments
        }
        return render(request, "Products/product_details.html",context)
        
    if request.method == "POST":
        user=request.user
        product = get_object_or_404(Product, id=product_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
        return redirect("product:detailproduct")
    else:
        return redirect("product:detailproduct")
