# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from blogs.models import Blog
from blogs.settings import PUBLISHED
from blogs.forms import BlogForm
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import View, ListView
from django.db.models import Q     # Q para OR en queries ... filter(Q(id=X) | Q(id=Y))



class BlogsQueryset(object):
    def get_blogsQuerySet(self, request, ownerName):
        if not request.user.is_authenticated():
            blogs = Blog.objects.filter(status=PUBLISHED)
        elif request.user.is_superuser:
            blogs = Blog.objects.all()
        else:
            blogs = Blog.objects.filter(Q(owner=request.user) | Q(status=PUBLISHED))

        if ownerName is not None:
            blogs = blogs.filter(owner__username=ownerName)

        if request.method != 'GET' and not request.user.is_superuser:
            blogs = blogs.filter(owner=request.user)

        return blogs

class HomeView(View, BlogsQueryset):
    def get(self, request):
        """
        Home of WorldPlease
        :param request: HttpRequest
        :return: HttpResponse
        """
        blogs = self.get_blogsQuerySet(request, None).order_by('-modified_at').select_related('owner')

        context = {
            'blogs_list': blogs[:10],
        }

        return render(request, 'blogs/home.html', context)

class DetailView(View, BlogsQueryset):
    def get(self, request, ownerName, pk):
        """
        Detalle de un articulo
        :param request: HttpRequest
        :param pk: id blog
        :return: HttpResponse
        """
        blog_req = self.get_blogsQuerySet(request, ownerName).filter(pk=pk).select_related('owner')
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

class AuthorView(View, BlogsQueryset):
    def get(self, request, ownerName):
        """
        Detalle de un autor
        :param request: HttpRequest
        :param ownerName: owner User
        :return: HttpResponse
        """

        consulted_owner = User.objects.filter(username=ownerName)
        if len(consulted_owner) < 1:
            return HttpResponseNotFound("Error 404 Not Found")

        blogs = self.get_blogsQuerySet(request, ownerName).order_by('-created_at').select_related('owner')

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
    #@method_decorator(login_required())
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

    #@method_decorator(login_required())
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

class EditView(View):
    #@method_decorator(login_required())
    def get(self, request, ownerName, pk):
        """
        Shows a form to create a new blog
        :param request: HttpRequest
        :return: HttpRequest
        """
        if request.user.is_superuser or request.user.username == ownerName:
            if request.user.is_superuser:
                blog_req = Blog.objects.filter(pk=pk)
            else:
                blog_req = Blog.objects.filter(pk=pk, owner=request.user)

            if len(blog_req) >= 1:
                blog = blog_req[0]
            else:
                return HttpResponseNotFound("Error 404 Not Found")

            form = BlogForm(instance=blog)

            context = {
                'form': form
            }

            return render(request, 'blogs/new_blog.html', context)
        else:
            return HttpResponseNotFound("Error 404 Not Found")


    #@method_decorator(login_required())
    def post(self, request, ownerName, pk):
        """
        Shows a form to create a new blog
        :param request: HttpRequest
        :return: HttpRequest
        """
        if request.user.is_superuser or request.user.username == ownerName:
            if request.user.is_superuser:
                blog_req = Blog.objects.filter(pk=pk)
            else:
                blog_req = Blog.objects.filter(pk=pk, owner=request.user)

            if len(blog_req) >= 1:
                blog = blog_req[0]
            else:
                return HttpResponseNotFound("Error 404 Not Found")
        else:
            return HttpResponseNotFound("Error 404 Not Found")

        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            new_blog = form.save() # Guarda el objeto y lo devuelve FTW
            return redirect('blog_detail', ownerName=new_blog.owner, pk=new_blog.pk)

        context = {
            'form': form
        }
        return render(request, 'blogs/new_blog.html', context)


class MyBlogView(ListView):
    model = Blog
    template_name = 'blogs/my_blog.html'

    #@method_decorator(login_required())
    def get_queryset(self):
        queryset = super(MyBlogView, self).get_queryset()
        return queryset.filter(owner=self.request.user).order_by('-created_at').select_related('owner')


class NotFoundView(View):
    def get(self, request):
        return HttpResponseNotFound("Error 404 Not Found")
    def post(self, request):
        return HttpResponseNotFound("Error 404 Not Found")