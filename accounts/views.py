from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, UserCreateForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TopPageView(TemplateView):
    template_name = 'top_page/top_page.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login_page.html'


class UserCreate(CreateView):
    template_name = 'accounts/user_create.html'
    form_class = UserCreateForm

    def get_success_url(self):
        Login()
        target = 'post:post'
        return reverse(target)


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/login_page.html'
