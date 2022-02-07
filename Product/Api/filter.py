
from django_filters.rest_framework import FilterSet
from Product.models import Product

class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'price':['range'],
            

        }
