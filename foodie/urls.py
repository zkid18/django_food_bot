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
    path('posts/', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('', PostList.as_view(), name='list'),
    path('bot/webhook', csrf_exempt(BotView.as_view())),
]

handler404 = 'posts.views.custom_404_error'

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
