from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm


# from .filters import PostFilter


def home(request):
    posts = Post.objects.filter(active=True, featured=False)[0:3]
    context = {'posts': posts}
    return render(request, 'base/index.html', context)


def posts(request):
    posts = Post.objects.all()
    # postFiler = PostFilter(request.GET, queryset=posts)
    # posts = postFiler.qs

    page = request.GET.get('page')

    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts}
    return render(request, 'base/posts.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'base/post.html', context)


def profile(request):
    return render(request, 'base/profile.html')


# CRUD VIEWS
@login_required(login_url="home")
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url="home")
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)


@login_required(login_url="home")
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    context = {'item': post}
    return render(request, 'base/delete.html', context)
