# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from users.forms import LoginForm

def login(request):
    error_messages = []
    if request.method == 'POST':
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
    else:
        form = LoginForm()
    context = {
        'errors': error_messages,
        'login_form': form
    }

    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)

    return redirect('blog_home')