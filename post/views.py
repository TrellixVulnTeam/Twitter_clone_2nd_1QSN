import random

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView
from .forms import PostCreateForm
from accounts.models import Post


class PostView(CreateView):
    template_name = 'post/post.html'
    model = Post
    success_url = '/post/'
    form_class = PostCreateForm

    def get_context_data(self, *args, **kwargs, ):
        Post_model = Post
        context = super(PostView, self).get_context_data(**kwargs)
        posts = self.model.objects.order_by('-created_data').filter(user_id=self.request.user.id)[:3]
        other_user_random_id = list(self.model.objects.exclude(user_id=self.request.user.id))
        random_id = random.sample(other_user_random_id,3)
        # print(other_user_random_id)
        post = Post()
        post.like = post.like + 1
        context['like'] = post
        context['other_user'] = random_id
        context['posts'] = posts
        return context

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = User.objects.get(id=request.user.id)
            new_post.save()
            return redirect('/post/')


class UserDetailView(ListView, Post):
    template_name = 'post/user_detail.html'
    model = Post
    Usermodel = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['posts'] = self.model.objects.filter(user_id=self.request.user.id)
        return context
