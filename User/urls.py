from django.urls import path
from django.urls.conf import re_path

from .views import forget_password, login, logout, register, activate,forget_pass,user_session_logedin
app_name="User"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("activate/<str:valid>", activate, name="activate"),
    path("forget_password/", forget_password, name="forget_password"),
    path("forget_pass/", forget_pass, name="forget_pass"),
    path("linked_dev/", user_session_logedin, name="user_session"),



]
