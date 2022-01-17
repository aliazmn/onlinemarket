
from .views import Home, searchbox
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls







    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',searchbox, name='serachbox'),
    path('' , Home.as_view() ,  name='home'),
    path('pro/',include('Product.urls')),
    path('comment/',include('Comment.urls', namespace='comment')),
    path('product/',include("Product.urls",namespace="product") ),
    path("", include("User.urls", namespace='user')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('payment/', include("Payment.urls",namespace="payment")),
    


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
