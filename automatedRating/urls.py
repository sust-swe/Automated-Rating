from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('posts.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
