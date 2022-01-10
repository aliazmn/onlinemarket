from django.contrib import admin

# Register your models here.
from Product.models import Category, Details, Product, Property, WishList

# Register your models here.
admin.site.register(Category)  
admin.site.register(Product) 

admin.site.register(WishList) 

class CartItemInline(admin.StackedInline):
    model = Details


@admin.register(Property)
class CartModelAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]




