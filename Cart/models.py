from django.db import models
from User.models import Customer, SalesMan
from Product.models import Product
from django.utils.translation import gettext as _



class CartMe(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='CartmetoCustomer',help_text="نام کاربری")
    product=models.ManyToManyField(Product,through="CartItem",help_text="کالاها")
    priceTotla=models.PositiveIntegerField(verbose_name=_("priceTotla"),null=True,blank=True)
    discount=models.CharField(max_length=10,verbose_name=_("discount"))
    date=models.DateTimeField(auto_now=True)
    ispaid=models.BooleanField(default=False)

    class Meta:
        verbose_name="Cart"
        verbose_name_plural="Carts"
    
    def __str__(self) -> str:
        return self.profile_ptr.username




class CartItem(models.Model):
    cart=models.ForeignKey(CartMe,on_delete=models.CASCADE,related_name='CartItemtoCartMe',help_text="سبد خرید")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='CartItemtoProduct',help_text="کالاها")
    salesman=models.ForeignKey(SalesMan,null=True,blank=True,on_delete=models.DO_NOTHING, related_name='cartitemtosels')
    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"




class History(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='HistorytoCustomer',help_text="مشتری")
    cartme=models.ManyToManyField(CartMe,help_text="کالاها")
    date=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    factor=models.JSONField(null=True,blank=True,verbose_name=_("factor"),help_text="فاکتور خرید")


    class Meta:
        verbose_name="History"
        verbose_name_plural="Historys"
    
    def __str__(self) -> str:
        return self.profile_ptr.username

    