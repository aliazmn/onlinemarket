

from django.urls import path
from Comment.Api.Comment_Api import CommentView
from Comment.views import add_comment


app_name='Comment'


urlpatterns = [
    path('comment/<int:product_id>', add_comment ,name='comment'),

    #Api
  path('commentapi/',CommentView.as_view(), name='commentapi')


]
