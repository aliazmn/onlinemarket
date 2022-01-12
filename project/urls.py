<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("", include("User.urls", namespace='user')),

    
=======

from django.urls.conf import include
from .views import Home, searchbox
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',searchbox, name='serachbox'),
    path('' , Home.as_view() ,  name='home'),
    path('pro/',include('Product.urls')),
    path('comment/',include('Comment.urls', namespace='comment')),
    path('product/',include("Product.urls",namespace="product") ),


>>>>>>> 1be6c836f417ba9a945f338c8dee82dda93cf4a6
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
