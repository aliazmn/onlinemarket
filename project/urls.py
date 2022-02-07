
from .views import Home, searchbox
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views





    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',searchbox, name='serachbox'),
    path('' , Home.as_view() ,  name='home'),
    path('comment/',include('Comment.urls', namespace='comment')),
    path('product/',include("Product.urls",namespace="product") ),
    path("", include("User.urls", namespace='user')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('payment/', include("Payment.urls",namespace="payment")),
    path('cart/', include("Cart.urls",namespace="cart")),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('oauth/', include('social_django.urls', namespace='social'))

]

#1651374
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
