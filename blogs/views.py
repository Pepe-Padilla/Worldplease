# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from blogs.models import Blog
from blogs.settings import PUBLISHED
from blogs.forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View

class HomeView(View):
    def get(self, request):
        """
        Home of WorldPlease
        :param request: HttpRequest
        :return: HttpResponse
        """
        blogs = Blog.objects.filter(status=PUBLISHED).order_by('-created_at').select_related('owner')

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

        return render(request, 'blogs/blog_list.html', context)

class DetailView(View):
    def get(self, request, ownerName, pk):
        """
        Detalle de un articulo
        :param request: HttpRequest
        :param pk: id blog
        :return: HttpResponse
        """
        consulted_owner = User.objects.filter(username=ownerName)[0]

        blog_req = Blog.objects.filter(
            pk=pk,
            owner=consulted_owner
        ).select_related('owner')
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

class AuthorView(View):
    def get(self, request, ownerName):
        """
        Detalle de un autor
        :param request: HttpRequest
        :param ownerName: owner User
        :return: HttpResponse
        """
        consulted_owner = User.objects.filter(username=ownerName)[0]
        blogs = Blog.objects.filter(owner=consulted_owner).order_by('-created_at').select_related('owner')

        titleHead = ownerName
        titleSection = 'Last WorldPlease publications of ' + ownerName
        title = {
            'head': titleHead,
            'section': titleSection
        }

        context = {
            'blogs_list': blogs[:10],
            'title': title
        }

        return render(request, 'blogs/blog_list.html', context)

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
        blog_with_owner = Blog()
        blog_with_owner.owner = request.user
        form = BlogForm(request.POST, instance=blog_with_owner)
        if form.is_valid():
            new_blog = form.save() # Guarda el objeto y lo devuelve FTW
            return redirect('blog_detail', ownerName=new_blog.owner, pk=new_blog.pk)

    context = {
        'form': form
    }
    return render(request, 'blogs/new_blog.html', context)