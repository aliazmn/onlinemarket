from django.utils.translation import gettext as _
from User.models import Profile
from django.db import models
from django.utils.text import slugify
from django.shortcuts import get_object_or_404


import Comment

class Category(models.Model):
    cat_title=models.CharField(max_length=150)
    sub_cat=models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='cattocat')

    @classmethod
    def get_cat(cls,id):
        cat = get_object_or_404 (Category,pk = id)
        return cat

    
    def __str__(self) -> str:
        return self.cat_title


class Product(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField(null=True)
    brand=models.CharField(max_length=50,null=True ,blank=True)
    price=models.BigIntegerField(null=True)
    amount=models.PositiveIntegerField(null=True)
    activate=models.BooleanField(default=False)
    img=models.ImageField(upload_to="Products/",null=True,blank=True)
    img1=models.ImageField(upload_to="Products/",null=True,blank=True)
    img2=models.ImageField(upload_to="Products/",null=True,blank=True)
    date_create=models.DateField(auto_now_add=True)
    data_update=models.DateField(auto_now=True)
    cat_id=models.ForeignKey(Category, on_delete=models.CASCADE,  related_name='producttocat' )
    slug = models.SlugField(null=True, unique=True, blank=True)


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @property
    def return_category(self):
        cat=Category.objects.get(pk=self.cat_id.id)
        return cat

    @property
    def comments(self):
        if self.id:
            return Comment.models.CommentMe.objects.filter(product_id=self.id)
        return None
    
    
    def __str__(self) -> str:
        return f"{self.name}-{self.brand}"


    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)
         

class Property(models.Model):
    property_name=models.CharField(max_length=50,null=True,blank=True)
    cat_id=models.ForeignKey(Category,on_delete=models.CASCADE, null=True,blank=True,related_name='propertytocat')
    
    def __str__(self) -> str:
        return self.property_name



class Details(models.Model):
    pro_id=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='detailstoproperty')
    product_id=models.ManyToManyField(Product)
    detail=models.CharField(max_length=400 ,null=True,blank=True) 

    def __str__(self) -> str:
        return self.detail
    

class WishList(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="wishlisttocustomer")
    product=models.ManyToManyField(Product)
    datetime =models.DateTimeField(auto_now=True,verbose_name=_('date and time'))

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"


