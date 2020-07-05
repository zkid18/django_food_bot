from django.test import TestCase
from posts.models import Post
from django.core.files import File
from django.contrib.auth.models import User
from django.utils import timezone

# Create your tests here.
class PostTests(TestCase):
    def setUp(self):
        self.description = "sample description"
        self.author = User.objects.create_user(
            username='user_name', email='soos@i.com', password='vvggtt'
            )
        self.image = File(open('media/y38.jpg', 'rb'))
        Post.objects.create(description=self.description,
                            author=self.author,
                            image=self.image,
                            created=timezone.now(),
                            modified=timezone.now()
                            )
    
    def test_creation(self):
        post = Post.objects.get(id=1)
        self.assertTrue(isinstance(post, Post))
    
    def test_slug(self):
        post = Post.objects.get(id=1)
        expected_slug = self.description.replace(' ', '-') + '-' + timezone.now().strftime('%Y-%m-%d')
        self.assertEquals(post.slug, expected_slug)
