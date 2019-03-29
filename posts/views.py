# from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .permissions import IsAuthororReadOnly
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthororReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
