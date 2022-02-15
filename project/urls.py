from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views


from rest_framework.routers import DefaultRouter

from azbankgateways.urls import az_bank_gateways_urls

from Comment.Api.Comment_Api import CommentView
from .views import Home, searchbox
from Product.Api.Product_api import CategoryListViewSet



router = DefaultRouter()

router.register(r'categorylist', CategoryListViewSet, basename='categorylist'),
# router.register(r'CommentView', CommentView, basename='CommentView')
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',searchbox, name='serachbox'),
    path('' , Home.as_view() ,  name='home'),
    path('comment/',include('Comment.urls', namespace='comment')),
    path('product/',include("Product.urls",namespace="product") ),
    path("user/", include("User.urls", namespace='user')),
    path('payment/', include("Payment.urls",namespace="payment")),
    path('cart/', include("Cart.urls",namespace="cart")),
    # path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('oauth/', include('social_django.urls', namespace='social'))

]+router.urls   



#1651374
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


