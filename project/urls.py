from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework.routers import DefaultRouter


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

]+router.urls   


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


