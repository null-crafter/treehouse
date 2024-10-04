import os

from core.utils import Post, loaded_posts
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def post_list(request):

    return render(request, "core/posts.html", {"posts": loaded_posts.values()})


def post_single(request, slug: str):
    post = loaded_posts.get(slug)
    if post is None:
        raise Http404()
    return render(request, "core/post_single.html", {"post": post})
