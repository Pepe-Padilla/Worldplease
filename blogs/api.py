# -*- coding: utf-8 -*-
#from rest_framework.views import APIView
#from rest_framework.response import Response
from blogs.models import Blog
from blogs.serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#from django.shortcuts import get_object_or_404
#from rest_framework import status

class BlogListAPI(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer