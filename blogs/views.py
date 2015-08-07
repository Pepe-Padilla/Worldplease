# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseNotFound
from blogs.models import Blog, PUBLISHED

def home(request):

    blogs = Blog.objects.filter(status=PUBLISHED).order_by('-created_at')

    context = {
        'blogs_list': blogs[:10]
    }

    return render(request, 'blogs/home.html', context)

def detail(request, ownerName, pk):
    """
    Detalle de un articulo
    :param request: HttpRequest
    :param pk: id blog
    :return: HttpResponse
    """
    an = 1
    blog_req = Blog.objects.filter(
        pk=pk,
        #owner=ownerName
    )
    blog = blog_req[0] if len(blog_req) >= 1 else None

    if blog is not None:
        #crear contexto
        context = {
            'blog': blog
        }
        #plantilla de detalle
        return render(request,'blogs/detail.html', context)
    else:
        return HttpResponseNotFound("Error 404 Not Found")