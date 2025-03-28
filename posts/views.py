from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.filter(status='PUBLISHED')
    return render(request, 'posts/index.html', context={'posts': posts})

def post_details(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, 'posts/detail.html', context={'post': post})