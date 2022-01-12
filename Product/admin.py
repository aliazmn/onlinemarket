from django.contrib import admin
from Product.models import Category, Details, Product, Property, WishList
from Product.models import Category, Details, Product, Property, WishList


admin.site.register(Category)  
admin.site.register(Product) 
admin.site.register(WishList) 

class CartItemInline(admin.StackedInline):
    model = Details


@admin.register(Property)
class CartModelAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]




