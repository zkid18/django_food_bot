from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from posts.models import Post

class PostList(ListView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'description']
    success_url = '/'
    login_url = '/accounts/login'
