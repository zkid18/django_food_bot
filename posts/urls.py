from django.conf.urls import url
from django.urls import path, include
from posts.views import PostCreate, PostLikeToggle, PostDetail, PostList, PostEdit

app_name = 'posts'

urlpatterns = [
    path("", PostList.as_view(), name="list"),
    path('new/', PostCreate.as_view(), name='new'),
    path('<pk>/edit/', PostEdit.as_view(), name='edit'),
    path("<pk>/like/", PostLikeToggle.as_view(), name='like'),
    path("<pk>/", PostDetail.as_view(), name='detail')
]
