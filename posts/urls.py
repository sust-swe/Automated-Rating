from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('archives/', views.archives, name='archives'),
    path('details/<int:id>/', views.details, name='details'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('like/', views.like_post, name='like_post'),
    path('updaterating/', views.updaterating, name='updaterating'),
    path('archivesgrid/', views.archives_grid, name='archives_grid')
]
