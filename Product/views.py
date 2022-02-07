

from django.shortcuts import render,redirect
from django.views.generic import DetailView,ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator


from User.models import Profile
from .models import Product,Category,Details,Property,WishList
from Comment.models import CommentMe
from Comment.forms import CommentForm
from .utils import property_and_details , color_property , filter_product_with_param,filtering


User = get_user_model()

class ProductDetail(DetailView):
    model=Product
    template_name = "Product/product_details.html"
    context_object_name = "singleproduct"
    pk_url_kwarg = "product_id"

    def get_context_data(self, *args, **kwargs):
        ctnx = super().get_context_data(*args, **kwargs)
        
        cat = self.get_object().return_category
        ctnx["cat"] = cat

        ctnx["color"] = color_property(self.kwargs["product_id"])
        ctnx["property"] = property_and_details(self.kwargs["product_id"],cat)
        
        ctnx["listproduct"] = filter_product_with_param (cat_id=cat)
        
        comments = self.get_object().comments

        ctnx["form"] = CommentForm()
        ctnx["comment"] = comments
        return ctnx




class ShowProduct(ListView):
    model = Product
    template_name = "Product/product_category.html"
    context_object_name = "productlist"
    paginate_by = 8

    def get_queryset(self) :
        qs = super().get_queryset()
        if len(self.request.GET)>1:
           qs = filtering(self.request.GET)                
            
        else:    
            qs = filter_product_with_param(cat_id_id = self.request.GET.get("c"))
            
        return qs

    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx["category"] = Category.get_cat(self.request.GET.get("c"))
        ctx["c_get"] = self.request.GET.get("c")
        return ctx







@login_required(login_url='/user/login')
def add_to_wishlist(request):
    user=get_object_or_404(Profile, email=request.user.email)
    my_wishlist,_=WishList.objects.get_or_create(user=user)
    product= get_object_or_404(Product, id=request.POST.get("id"))
    my_wishlist.product.add(product)
    my_wishlist.save()
    return redirect("product:detailproduct", product_id=request.POST.get("id") )

@login_required(login_url='/user/login')
def delete_from_wishlist(request,id):
    object_product=get_object_or_404(Product,pk=id)
    wishlist=get_object_or_404(WishList,product=id)
    wishlist.product.remove(object_product)
    return redirect("product:Show_wishList")
 

@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class Show_wishList(ListView):
    model=WishList
    template_name="Product/wishlist.html"
    context_object_name="wish_list"

    def get_queryset(self) :
        qs=WishList.objects.filter(user = self.request.user).first()
        
        return qs
       
