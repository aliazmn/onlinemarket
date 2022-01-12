
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from Product.models import Product

from .views import Home, searchbox


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',searchbox, name='serachbox'),
    path('' , Home.as_view() ,  name='home'),
    path('pro/',include('Product.urls')),
    path('comment/',include('Comment.urls', namespace='comment')),
]

