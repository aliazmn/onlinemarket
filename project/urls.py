from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("", include("User.urls", namespace='user')),

    
]
