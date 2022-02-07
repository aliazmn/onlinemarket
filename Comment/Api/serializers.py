from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import serializers

from Comment.models import CommentMe
from Product.models import Product

User = get_user_model()
class CommentSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only = True)

    class Meta:
        model = CommentMe
        fields = ['comment', 'product','user']

    def create(self, validated_data):
        print("too  createe serilize omadammmmm")

        obj=super().create(validated_data)
        print(obj)
        email=self.context["request"].user.email
        print(email)
        user=get_object_or_404(User,email =email )

        obj.user = user

        obj.save()

        return obj