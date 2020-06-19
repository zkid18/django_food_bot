from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from posts.views import PostList, PostCreate, PostLikeToggle, PostDetail
from telebot_api.views import BotView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('new/', PostCreate.as_view(), name='new'),
    path('', PostList.as_view(), name='list'),
    path('posts/', PostList.as_view(), name='list'),
    path('posts/<pk>/like/', PostLikeToggle.as_view(), name='like'),
    path('posts/<pk>/', PostDetail.as_view(), name='detail'),
    path('bot/webhook', csrf_exempt(BotView.as_view())),
]

handler404 = 'posts.views.custom_404_error'

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
