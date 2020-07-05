from django.db import models
from django.contrib.auth.models import User, UserManager
from django.urls import reverse
from django.template.defaultfilters import slugify
import random
import string


def randomString():
    um = UserManager()
    return( um.make_random_password(length=25))

class Post(models.Model):
    image = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300)
    likes = models.ManyToManyField('Like', related_name='post_likes')

    class Meta: 
       ordering = ('-created', '-modified', ) 

    def save(self, *args, **kwargs):
        slug = slugify(self.description + '-' + self.created.strftime('%Y-%m-%d'))
        # slug = ''.join(random.sample(string.ascii_lowercase, 10))
        self.slug = slug
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self, pk):
        return reverse("posts:detail", kwargs={"pk": pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)



