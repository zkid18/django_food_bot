from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404
from django.db import transaction
# Create your views here.
from posts.models import Post

class PostList(ListView):
    model = Post

class PostLikeToggle(RedirectView):
    @transaction.atomic
    def get_redirect_url(self, *args, **kwargs):
        post_id = kwargs.get('pk')
        post = get_object_or_404(Post, id=post_id)
        user = self.request.user
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        url_redirect = post.get_absolute_url(post_id)
        return url_redirect

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'description']
    template_name = 'posts/post_new.html'
    success_url = '/'
    login_url = '/accounts/login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEdit(UpdateView):
    model = Post
    fields = ['image', 'description']
    template_name = 'posts/post_edit.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
        
def custom_404_error(request, exception):
    print(request.path)
    data = {
        'method': request.method,
        'uri': request.path
        }
    return render(request,  'post_404.html', data)