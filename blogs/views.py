# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog

def home(request):

    blogs = Blog.objects.all()



    #html = '<ul>'
    #for blog in blogs:
    #    html += '<li>' + blog.title + '</li>'
    #html += '<ul>'

    return render(request, 'blogs/home.html')