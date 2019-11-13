from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.template.loader import render_to_string

from .models import Posts, Comment
from .choices import rating_choices, category_choices, postcriteria_choices
from . import forms

# Create your views here.


def index(request):
    # return HttpResponse('hello from posts')

    posts = Posts.objects.order_by('-created_at')
    postd = Posts.objects.order_by('-created_at')
    if request.method =="POST":
        query = request.POST['q']
        if query:
            posts = Posts.objects.filter(title__icontains=query)
            postd = Posts.objects.filter(body__icontains=query)


    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'title': 'Recent Posts',
        'rating_choices': rating_choices,
        'category_choices': category_choices,
        'postcriteria_choices': postcriteria_choices,
        'posts': paged_posts,
        'postd':postd
    }

    return render(request, 'posts/index.html', context)


def archives(request):

    posts = Posts.objects.order_by('-created_at')

    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'title': 'Recent Posts',
        'posts': paged_posts
    }

    return render(request, 'posts/archives.html', context)

def archives_grid(request):

    posts = Posts.objects.order_by('-created_at')

    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'title': 'Recent Posts',
        'posts': paged_posts
    }

    return render(request, 'posts/archive-grid-1.html', context)


def details(request, id):
    post = Posts.objects.get(id=id)
    next_post = Posts.objects.filter(id__gt=post.id).order_by('id').first()
    prev_post = Posts.objects.filter(id__gt=post.id).order_by('id').first()
    comments = post.comments.all()

    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    # For Comment Form
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect("login")
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.post = post
            instance.save()
            return redirect("details", id=post.id)

    form = forms.CommentForm()

    context = {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
        'form': form,
        'comments': comments,
        'is_liked': is_liked,
    }

    return render(request, 'posts/details.html', context)

@login_required(login_url="login")
def like_post(request):
    # id = request.POST.get('post_id')
    id = request.POST.get('id')
    post = get_object_or_404(Posts, id=id)
    is_liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    context = {
        'post': post,
        'is_liked': is_liked,
    }
    if request.is_ajax():
        html = render_to_string('posts/like_section.html', context, request=request)
        return JsonResponse({'form': html})


@login_required(login_url="login")
def create(request):
    if request.method == 'POST':
        # request.files for image
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('index')

    else:
        form = forms.CreatePost()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)


def search(request):

    queryset_list = Posts.objects.order_by('-created_at')

    #keywords=avenger&author=fsda&category=Game&postcriteria=mpp&rating=5
    # Keywords for existing in all fields
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(title__icontains=keywords) |
                                                 Q(body__icontains=keywords) |
                                                 Q(slug__icontains=keywords) |
                                                 Q(post_item__item_category__category_name=keywords) |
                                                 Q(post_item__ItemsList_name=keywords) |
                                                 Q(author__username=keywords) |
                                                 Q(author__first_name=keywords))

    # Author
    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            queryset_list = queryset_list.filter(Q(author__username=author) |
                                                 Q(author__first_name=author))

    #Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(post_item__item_category__category_name=category)
    
    #postcriteria
    if 'postcriteria' in request.GET:
        postcriteria = request.GET['postcriteria']
        if postcriteria:
            queryset_list = queryset_list.filter(postcriteria = postcriteria)

    #rating for equal or greater number
    if 'rating' in request.GET:
        rating = request.GET['rating']
        if rating:
            queryset_list = queryset_list.filter(post_item__rating__gte = rating)

    context = {
        'title': 'Search Results',
        'rating_choices': rating_choices,
        'category_choices': category_choices,
        'postcriteria_choices': postcriteria_choices,
        'posts': queryset_list,
        'values': request.GET,
    }

    return render(request, 'posts/search.html', context)
