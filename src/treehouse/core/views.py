import os
from datetime import timezone

from core.utils import Post, loaded_posts
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.templatetags.static import static


def favicon(request):
    return redirect(static("favicon.ico"), permanent=False)


# Create your views here.
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def post_list(request):

    return render(
        request,
        "core/posts.html",
        {
            "posts": sorted(
                loaded_posts.values(),
                key=lambda p: -p.date.replace(tzinfo=timezone.utc).timestamp(),
            )
        },
    )


def post_single(request, slug: str):
    post = loaded_posts.get(slug)
    if post is None:
        raise Http404()
    return render(request, "core/post_single.html", {"post": post})
