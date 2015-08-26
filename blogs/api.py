# -*- coding: utf-8 -*-
#from rest_framework.response import Response
from blogs.models import Blog
from blogs.serializers import BlogSerializer, BlogListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blogs.views import BlogsQueryset

#from django.shortcuts import get_object_or_404
#from rest_framework import status

class BlogListAPI(BlogsQueryset, ListCreateAPIView):
    #queryset = Blog.objects.all().order_by('-modified_at')
    permission_classes = (IsAuthenticatedOrReadOnly,)

    #serializer_class = BlogListSerializer

    def get_serializer_class(self):
        return BlogSerializer if self.request.method == 'POST' else BlogListSerializer

    def get_queryset(self):
        return self.get_blogsQuerySet(self.request, None).order_by('-modified_at')

class BlogDetailAPI(BlogsQueryset, RetrieveUpdateDestroyAPIView):
    #queryset = Blog.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = BlogSerializer

    def get_queryset(self):
        return self.get_blogsQuerySet(self.request, None)