# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from users.forms import LoginForm, SignUpForm
from django.views.generic import View
from django.contrib.auth.models import User

class bloguersView(View):
    def get(self, request):
        users = User.objects.all().order_by('username')

        context = {
            'users_list': users
        }

        return render(request, 'users/bloguers.html', context)


class LoginView(View):
    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }

        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Wrong user name or password')
            else:
                if user.is_active:
                    django_login(request,user)
                    url = request.GET.get('next', 'blog_home')
                    return redirect(url)
                else:
                    error_messages.append('User not active')

        context = {
            'errors': error_messages,
            'login_form': form
        }

        return render(request, 'users/login.html', context)

class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        context = {
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)

    def post(self, request):

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_login')

        error_messages = ['Signup not valid',]
        context = {
            'errors': error_messages,
            'signup_form': form
        }

        return render(request, 'users/signup.html', context)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)

        return redirect('blog_home')