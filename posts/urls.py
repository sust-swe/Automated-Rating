from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name='about'),
    path('details/<int:id>/', views.details, name = 'details')
]