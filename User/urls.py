from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import *
from User.api.views import Login_api,logout_api,RegisterView


app_name="User"

urlpatterns = [
#----------------restless url----------------------
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register/", register, name="register"),
    path("activate/<str:valid>", activate, name="activate"),
    path("forget_password/", forget_password, name="forget_password"),
    path("forget_pass/", forget_pass, name="forget_pass"),
    path("set_true/<str:auten>", set_true, name="set_true"),
    path('profile/<int:id>',show_profile.as_view(),name="profile"),
#----------------linked divice---------------
    path("linked_dev/", user_session_logedin, name="user_session"),
#---------------API-----------------------
    path("api/login/",Login_api.as_view(), name="api-login"),
    path("api/register",RegisterView.as_view()),
    path("api/logout",logout_api),
#--------------jwt token---------------------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
