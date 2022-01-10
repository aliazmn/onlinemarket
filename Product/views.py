
from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Product,Category,Details,Property
from django.db.models import Q



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
        property_size=Property.objects.get(property_name="سایزلباس")
        detail_size=Details.objects.filter(Q(product_id=self.kwargs["product_id"]) & Q(pro_id=property_size.id))
        ctnx["size"]=detail_size

        product_best=Product.objects.filter(cat_id=cat)
        ctnx["listproduct"]=product_best


        return ctnx



class ShowProduct(ListView):
    model=Product
    template_name="Product/product_category.html"
    context_object_name="productlist"
    paginate_by=2

    def get_queryset(self) :
        qs= super().get_queryset()
        qs=Product.objects.filter(cat_id_id=self.request.GET.get("c"))
        return qs

    def get_context_data(self, **kwargs):
        ctx= super().get_context_data(**kwargs)
        ctx["category"]=Category.objects.get(pk=self.request.GET.get("c"))
        ctx["fcategory"]=ctx["category"].sub_cat.cat_title
        ctx["c_get"]=self.request.GET.get("c")
        return ctx

    