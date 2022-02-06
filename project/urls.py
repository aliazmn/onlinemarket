from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from azbankgateways.urls import az_bank_gateways_urls
from .views import Home, searchbox
from project.Api.Home_api import SearchProductList
from Product.Api.Product_api import CategoryViewSet



router = DefaultRouter()

router.register(r'seearch', SearchProductList, basename='seearch')
router.register(r'category', CategoryViewSet, basename='category')




    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',searchbox, name='serachbox'),
    path('' , Home.as_view() ,  name='home'),
    path('comment/',include('Comment.urls', namespace='comment')),
    path('product/',include("Product.urls",namespace="product") ),
    path("user/", include("User.urls", namespace='user')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('payment/', include("Payment.urls",namespace="payment")),
    path('cart/', include("Cart.urls",namespace="cart")),

 
]+router.urls   


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


