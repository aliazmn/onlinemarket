from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.base_user import BaseUserManager








class Profile(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    


 


class Address(models.Model):
    add=models.CharField(max_length=255,verbose_name=_("address"),help_text="ادرس خود را وارد کنید")
    postalcode=models.CharField(max_length=10, verbose_name = _("postalcode"),)

    class Meta:
        verbose_name="Address"
        verbose_name_plural="Addresses"

    def __str__(self) -> str:
        return self.add        


class Admin(models.Model):
    add=models.ManyToManyField(Address)
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name="admintoprofile")


    class Meta:
        verbose_name="Admin"
        verbose_name_plural="Admins"


    def __str__(self) -> str:
        return self.profile_ptr.firstname



class Customer(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name="customertoprofile")
    add=models.ManyToManyField(Address)


    class Meta:
        verbose_name="Customer"
        verbose_name_plural="Customers"
        



    def __str__(self) -> str:
        return self.profile_ptr.firstname


class SalesMan(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE,related_name="salestoprofile")

    legal_information=models.CharField(max_length=255,verbose_name=_("legalinformation"),help_text="اطلاعات حقوقی خود را وارد کنید")
    cart_number=models.CharField(max_length=100,verbose_name=_("Arithmetic information"),help_text="اطلاعات حسابی خود را وارد کنید")
    add=models.ManyToManyField(Address)
    product=models.ManyToManyField(to="Product.Product")


    class Meta:
        verbose_name="SalesMan"
        verbose_name_plural="SalesMans"
        

    def __str__(self) -> str:
        return self.profile_ptr.firstname


