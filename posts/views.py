from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Posts

# Create your views here.


def index(request):
    #return HttpResponse('hello from posts')

    posts = Posts.objects.all()[:10]

    context = {
        'title' : 'Recent Posts',
        'posts' : posts
    }

    return render(request, 'posts/index.html', context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post' : post 
    }

    return render(request, 'posts/details.html', context)


@login_required(login_url="login")
def create(request):
    return render(request, 'posts/create.html')

