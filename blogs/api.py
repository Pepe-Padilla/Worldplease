# -*- coding: utf-8 -*-
#from rest_framework.views import APIView
#from rest_framework.response import Response
from blogs.models import Blog
from blogs.serializers import BlogSerializer, BlogListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#from django.shortcuts import get_object_or_404
#from rest_framework import status

class BlogListAPI(ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-modified_at')
    #serializer_class = BlogListSerializer

    def get_serializer_class(self):
        return BlogSerializer if self.request.method == 'POST' else BlogListSerializer

class BlogDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer