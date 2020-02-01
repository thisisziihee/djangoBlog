from django.contrib import admin
from django.urls import path, include

from user.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name = 'register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/', include('post.urls')),
]
