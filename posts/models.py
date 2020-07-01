from django.db import models
from django.contrib.auth.models import User, UserManager
from django.urls import reverse

def randomString():
    um = UserManager()
    return( um.make_random_password(length=25))

class Post(models.Model):
    image = models.ImageField()
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True, editable=False, default=randomString)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def get_absolute_url(self, pk):
        return reverse("posts:detail", kwargs={"pk": pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)