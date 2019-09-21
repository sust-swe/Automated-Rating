from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Posts
from . import forms

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
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)   #request.files for image
        if form.is_valid():
            # save to db
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('index')

    else :
        form = forms.CreatePost()
        context = {
            'form' : form
        }
        return render(request, 'posts/create.html', context)
