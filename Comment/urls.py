

from django.urls import path
from Comment.views import add_comment,aa


app_name='Comment'


urlpatterns = [
    path('comment/<int:product_id>', add_comment ,name='comment'),
    path('s', aa ,name='aa'),




]
