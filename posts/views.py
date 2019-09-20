from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.

def index(request):
    #return HttpResponse('hello from posts')

    posts = Posts.objects.all()[:10]

    context = {
        'title' : 'Recent Posts',
        'posts' : posts
    }

    return render(request, 'pages/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post' : post 
    }

    return render(request, 'pages/details.html', context)

def about(request):
    return render(request, 'pages/about.html')
