# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    usr = forms.CharField(label='User Name')
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    firstname = forms.CharField(label="Nombre")
    lastname = forms.CharField(label="Apellidos")
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "firstname", "lastname", "email")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user