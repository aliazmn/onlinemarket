from django.db import models
from User.models import Customer, Profile
from Product.models import Product
from django.utils.translation import gettext as _



class rate(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="ratetocustomer",verbose_name=_("user"))
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="ratetoproduct",verbose_name=_("product"))
    RATE_CHOICES=[
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5")
    ] 
    rate=models.CharField(max_length=1,choices=RATE_CHOICES,verbose_name=_("rate"),help_text="امتیاز خود را وارد کنید",null=True,blank=True)

    class Meta:
        verbose_name="rate"
        verbose_name_plural="rates"

    def __str__(self) -> str:
        return f"{self.user.first_name}+{self.id}"        

class CommentMe(models.Model):
    user=models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL,related_name="commenttouser",verbose_name=_("comment"))   
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="commenttoproduct",verbose_name=_("product"))

    comment=models.CharField(max_length=255,verbose_name=_("comment"),help_text="کامنت خود را وارد کنید",null=True,blank=True)

    class Meta:
        verbose_name="comment"
        verbose_name_plural="comments"

    def __str__(self) -> str:
        return f"{self.id}"   