

from django.urls import path
from Comment.views import add_comment


app_name='Comment'


urlpatterns = [
    path('comment/<int:product_id>', add_comment ,name='comment'),

    #Api
    





]
