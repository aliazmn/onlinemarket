from django.shortcuts import render
from django.views.generic import DetailView,ListView
from django.db.models import Q

from .models import Product,Category,Details,Property
from Comment.models import CommentMe
from Comment.forms import CommentForm


class ProductDetail(DetailView):
    model=Product
    template_name="Product/product_details.html"
    context_object_name="singleproduct"
    pk_url_kwarg="product_id"

    def get_context_data(self, *args, **kwargs):
        ctnx = super().get_context_data(*args, **kwargs)
        
        cat=Category.objects.get(pk=self.get_object().cat_id.id)
        ctnx["parent_cat"]=cat.sub_cat.cat_title
               
        property_color=Property.objects.get(property_name="رنگ")
        detail_color=Details.objects.filter(Q(product_id=self.kwargs["product_id"]) & Q(pro_id=property_color.id))
        ctnx["color"]=detail_color

        properties=Property.objects.filter(cat_id=cat.sub_cat)
        lst_details=[]

        for elm in properties:

            details=Details.objects.filter(Q(product_id=self.kwargs["product_id"]) & Q(pro_id=elm.id))
            if details:
                lst_details.append(details)
        ctnx["detail"]=lst_details
        product_best=Product.objects.filter(cat_id=cat)
        ctnx["listproduct"]=product_best
        comments=CommentMe.objects.all().filter(product=self.kwargs["product_id"])
        ctnx["form"]=CommentForm()
        ctnx["comment"]=comments
        return ctnx



class ShowProduct(ListView):
    model=Product
    template_name="Product/product_category.html"
    context_object_name="productlist"
    paginate_by=8

    def get_queryset(self) :
        qs= super().get_queryset()
        qs=Product.objects.filter(cat_id_id=self.request.GET.get("c"))
        self.request.session["c"]=self.request.GET.get("c")
        return qs

    def get_context_data(self, **kwargs):
        ctx= super().get_context_data(**kwargs)
        ctx["category"]=Category.objects.get(pk=self.request.GET.get("c"))
        ctx["fcategory"]=ctx["category"].sub_cat.cat_title
        ctx["c_get"]=self.request.GET.get("c")
        return ctx


class Filtering(ListView):
    model=Product
    template_name="Product/product_category.html"
    context_object_name="productlist"
    paginate_by=8

    def get_queryset(self) :
        qs= super().get_queryset()
        filter_brand=self.request.GET.get("brand")
        filter_price=self.request.GET.get("price")
        p=filter_price.split(",")
        if filter_brand!="برند" and filter_price!="قیمت":
            p=filter_price.split(",")
            qs=Product.objects.filter(Q(cat_id_id=self.request.session.get("c")) & Q(brand=filter_brand)  &Q(price__range=(int(p[0]),int(p[1]))) )
        
        elif filter_brand!="برند" and filter_price=="قیمت": 
            qs=Product.objects.filter(Q(cat_id_id=self.request.session.get("c")) & Q(brand=filter_brand)  )

        elif filter_price!="قیمت" and filter_brand =="برند":
            p=filter_price.split(",")
            qs=Product.objects.filter(Q(cat_id_id=self.request.session.get("c")) & Q(price__range=(int(p[0]),int(p[1]))) )

        else :
            qs=Product.objects.filter(cat_id_id=self.request.session.get("c"))
        
        return qs

    def get_context_data(self, **kwargs):
        ctx= super().get_context_data(**kwargs)
        ctx["category"]=Category.objects.get(pk=self.request.session.get("c"))
        ctx["fcategory"]=ctx["category"].sub_cat.cat_title
        ctx["c_get"]=self.request.session.get("c")
        ctx["p_get"]=self.request.GET.get("price")
        ctx["b_get"]=self.request.GET.get("brand")

        return ctx
