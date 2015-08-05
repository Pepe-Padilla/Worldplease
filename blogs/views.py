# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Blog

def home(request):

    blogs = Blog.objects.all()

    context = {
        'blogs_list': blogs[:10]
    }

    return render(request, 'blogs/home.html', context)