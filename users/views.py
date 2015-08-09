# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login

def login(request):
    error_messages = []
    if request.method == 'POST':
        username = request.POST.get('usr')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)

        if user is None:
            error_messages.append('Wrong user name or password')
        else:
            if user.is_active:
                django_login(request,user)
                return redirect('blog_home')
            else:
                error_messages('User not active')

    context = {
        'errors': error_messages
    }

    return render(request, 'users/login.html', context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)

    return redirect('blog_home')