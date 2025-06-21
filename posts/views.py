from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.


def index(request):
    # posts = Post.objects.filter(status='PUBLISHED')
    posts = Post.published_posts()
    total_posts = Post.total_posts()
    paginator = Paginator(posts, per_page=2)
    # get the page number from url, query parameter
    page_number = request.GET.get('page')
    # get all posts from that page number
    posts = paginator.get_page(page_number)
    return render(request, 'posts/index.html', context={'posts': posts, 'total_posts': total_posts})


def post_details(request, year, month, day, post_slug):
    post = Post.objects.get(publish__year=year, publish__month=month, publish__day=day, slug=post_slug, status='PUBLISHED')
    return render(request, 'posts/detail.html', context={'post': post})