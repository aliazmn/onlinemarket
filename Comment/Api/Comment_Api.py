
from rest_framework.generics import  CreateAPIView

from Comment.Api.serializers import CommentSerializer
from Comment.models import CommentMe


class CommentView(CreateAPIView):
    queryset = CommentMe.objects.all()
    serializer_class = CommentSerializer