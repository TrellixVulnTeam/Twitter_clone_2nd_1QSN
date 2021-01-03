from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from .forms import LoginForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TopPageView(TemplateView):
    template_name = 'top_page/top_page.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login_page.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'accounts/login_page.html'
