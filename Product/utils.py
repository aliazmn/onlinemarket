import re
from django.db.models import Q

from .models import Property,Details,Product,Category



def color_property(product_id):
    property_color = Property.objects.get(property_name="رنگ")
    detail_color = Details.objects.filter(Q(product_id=product_id) & Q(pro_id=property_color.id))
    return detail_color


def property_and_details(product_id,cat):

    dict_details = {}
    properties = Property.objects.filter(cat_id=cat)
    for elm in properties:
        details = Details.objects.filter(Q(product_id=product_id) & Q(pro_id=elm.id))
        if details:
            dict_details[elm.property_name] = details
        else:
            dict_details[elm.property_name] = ""
            
    return dict_details


def filter_product_with_param(**kwargs):
    product_best=Product.objects.filter(**kwargs)
    return product_best


def filtering(filter_params):

    for key,value in filter_params.items():
        print(key,value)
        if key == "c":
            filtered_product = Product.objects.filter(cat_id_id=value)
        elif key == "price" :
            if value!= "": 
                price=value.split(",")
                filtered_product = filtered_product.filter(price__range=(int(price[0]),int(price[1])))
            else : continue
        elif key == "brand":
            if value!= "":
                filtered_product = filtered_product.filter(brand = value)
            else : continue
            
            
    return filtered_product