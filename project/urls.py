from django.contrib import admin
from django.urls import path,include , re_path
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views


from rest_framework.routers import DefaultRouter


from Comment.Api.Comment_Api import CommentView
from .views import Home, searchbox
from Product.Api.Product_api import CategoryListViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




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
    path('oauth/', include('social_django.urls', namespace='social')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]+router.urls   



#1651374
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


