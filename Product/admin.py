from django.contrib import admin

from Product.models import Category, Details, Product, Property, WishList

# Register your models here.
admin.site.register(Category)  
admin.site.register(Property) 
admin.site.register(Product) 
admin.site.register(Details) 
admin.site.register(WishList) 