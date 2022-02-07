


from multiprocessing import context
from rest_framework.generics import  CreateAPIView, ListCreateAPIView
from rest_framework import viewsets
from Comment.Api.serializers import CommentSerializer
from Comment.models import CommentMe
from Product.models import Product
from rest_framework.response import Response
from rest_framework.views import APIView

class CommentView(ListCreateAPIView):
    queryset=CommentMe.objects.all()
    serializer_class=CommentSerializer


    def create(self, request, *args, **kwargs):
        print("too  createe omadammmmm")
        serialize=CommentSerializer(data=request.data , context ={"request":request})
        if serialize.is_valid():
            print("too  serializerrr omadamm omadammmmm")

            serialize.save()
            return Response(serialize.data)
        
        else:
            return Response(serialize.errors)

 
