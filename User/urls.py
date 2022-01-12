from django.urls import path

from .views import login, logout, register, profile_user

app_name="User"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile_user, name="profile_user"),


]
