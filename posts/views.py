from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.
from posts.models import Post

class PostList(ListView):
    model = Post