from django.urls import path
from .views import forget_password, login, logout, register, activate,forget_pass,set_true,show_profile

app_name="User"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("activate/<str:valid>", activate, name="activate"),
    path("forget_password/", forget_password, name="forget_password"),
    path("forget_pass/", forget_pass, name="forget_pass"),
    path("set_true/<str:auten>", set_true, name="set_true"),
    path('profile/<int:id>',show_profile.as_view(),name="profile"),


]
