

from rest_framework import serializers

from Comment.models import CommentMe
from Product.models import Product

class CommentSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='slug', queryset=Product.objects.all())
    user=serializers.StringRelatedField(many=True)
    class Meta:
        model = CommentMe
        fields = ['comment', 'product','user']

