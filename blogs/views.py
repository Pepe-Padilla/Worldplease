# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from blogs.models import Blog
from blogs.settings import PUBLISHED
from blogs.forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import View
#from django.db.models import Q     # Q para OR en queries ... filter(Q(id=X) | Q(id=Y))

class HomeView(View):
    def get(self, request):
        """
        Home of WorldPlease
        :param request: HttpRequest
        :return: HttpResponse
        """
        blogs = Blog.objects.filter(status=PUBLISHED).order_by('-created_at').select_related('owner')

        context = {
            'blogs_list': blogs[:10],
        }

        return render(request, 'blogs/home.html', context)

class DetailView(View):
    def get(self, request, ownerName, pk):
        """
        Detalle de un articulo
        :param request: HttpRequest
        :param pk: id blog
        :return: HttpResponse
        """
        blog = blogById(request, ownerName, pk)

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

        blogs = blogsByOwner(request, ownerName)

        if blogs is None:
            return HttpResponseNotFound("Error 404 Not Found")

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

        return render(request, 'blogs/author.html', context)

class CreateView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
        Shows a form to create a new blog
        :param request: HttpRequest
        :return: HttpRequest
        """
        form = BlogForm()

        context = {
            'form': form
        }
        return render(request, 'blogs/new_blog.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Shows a form to create a new blog
        :param request: HttpRequest
        :return: HttpRequest
        """
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

class NotFoundView(View):
    def get(self, request):
        return HttpResponseNotFound("Error 404 Not Found")
    def post(self, request):
        return HttpResponseNotFound("Error 404 Not Found")


def blogsByOwner(request, ownerName):
    """
    Función que regresa los blogs de un usuario dependiendo del usuario autenticado
    - No autenticado u otro usuario: publicas
    - Autenticado y autor: todas
    :param request: HttpRequest
    :param ownerName: user consulted (string)
    :return: Blog List
    """
    consulted_owner = User.objects.filter(username=ownerName)

    if len(consulted_owner) < 1:
        return None

    consulted_owner = consulted_owner[0]

    if request.user.username == ownerName or request.user.is_superuser:
        blogs = Blog.objects.filter(owner=consulted_owner).order_by('-created_at').select_related('owner')
    else:
        blogs = Blog.objects.filter(owner=consulted_owner, status=PUBLISHED).order_by('-created_at').select_related('owner')

    return blogs


def blogById(request, ownerName, pk):

    if request.user.username == ownerName or request.user.is_superuser:
        blog_req = Blog.objects.filter(
            pk=pk,
            owner__username=ownerName,
        ).select_related('owner')
    else:
        blog_req = Blog.objects.filter(
            pk=pk,
            owner__username=ownerName,
            status=PUBLISHED
        ).select_related('owner')
    blog = blog_req[0] if len(blog_req) >= 1 else None

    return blog
