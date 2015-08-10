# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from blogs.models import Blog, PUBLISHED
from blogs.forms import BlogForm
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Home of WorldPlease
    :param request: HttpRequest
    :return: HttpResponse
    """
    blogs = Blog.objects.filter(status=PUBLISHED).order_by('-created_at')

    titleHead = 'Home'
    titleSection = 'Last WorldPlease publications'
    title = {
        'head': titleHead,
        'section': titleSection
    }

    context = {
        'blogs_list': blogs[:10],
        'title': title
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
            'blog': blog,
        }
        #plantilla de detalle
        return render(request,'blogs/detail.html', context)
    else:
        return HttpResponseNotFound("Error 404 Not Found")

def author(request, ownerName):
    """
    Detalle de un autor
    :param request: HttpRequest
    :param ownerName: owner User
    :return: HttpResponse
    """
    blogs = Blog.objects.filter(status=PUBLISHED).order_by('-created_at')

    titleHead = 'Home'
    titleSection = 'Last WorldPlease publications'
    title = {
        'head': titleHead,
        'section': titleSection
    }

    context = {
        'blogs_list': blogs[:10],
        'title': title
    }

    return render(request, 'blogs/home.html', context)

@login_required()
def create(request):
    """
    Shows a form to create a new blog
    :param request: HttpRequest
    :return: HttpRequest
    """
    if request.method == 'GET':
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save() # Guarda el objeto y lo devuelve FTW
            return redirect('blog_detail', ownerName= new_blog.owner, pk= new_blog.pk)

    context = {
        'form': form
    }
    return render(request, 'blogs/new_blog.html', context)