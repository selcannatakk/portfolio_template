from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'base/index.html')


def posts(request):
    posts = [
        {
            'headline': 'Laboratory Management System',
            'sub_headline': 'Designed built & mantained a the lab managment system for FOI Laboratories'
        },
        {
            'headline': 'Online Store - CoursePost Title',
            'sub_headline': 'Online store with paypal payments intergration and guest user shopping'
        },
        {
            'headline': 'Membership Website',
            'sub_headline': 'Modulized guide for online courses with step by step intructions<'
        },
    ]
    context = {'posts': posts}
    return render(request, 'base/posts.html', context)


def post(request):
    return render(request, 'base/post.html')


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
