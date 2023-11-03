from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def home(request):
    posts = Post.objects.filter(active=True, featured=False)[0:3]
    context = {'posts': posts}
    return render(request, 'base/index.html', context)


def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'base/posts.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'base/post.html', context)


def profile(request):
    return render(request, 'base/profile.html')

# def home(request):
#     return HttpResponse('<h2>home</h2>')
#
#
# def posts(request):
#     return HttpResponse('<h2>posts</h2>')
#
#
# def post(request):
#     return HttpResponse('<h2>post</h2>')
#
#
# def profile(request):
#     return HttpResponse('<h2>profile</h2>')
