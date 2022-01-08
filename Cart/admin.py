from django.contrib import admin

from .models import CartMe, CartItem


class CartItemInline(admin.StackedInline):
    model = CartItem


@admin.register(CartMe)
class CartModelAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

