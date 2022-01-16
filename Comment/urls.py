

from django.urls import path
from Comment.views import add_comment, detail,aa,aa1


app_name='Comment'


urlpatterns = [
    path('comment/<int:product_id>', add_comment ,name='comment'),
    path('sd', aa ,name='aa'),
    path('sd1', aa1 ,name='aa1'),


]
