import os
from datetime import timezone

from core.utils import Post, loaded_posts
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.templatetags.static import static
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def favicon(request):
    return redirect(static("favicon.ico"))


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def github(request):
    github_url = getattr(settings, "SOCIALS", {}).get("github")
    validate_url = URLValidator(schemes=["https", "http"])
    try:
        validate_url(github_url)
    except ValidationError:
        raise Http404()
    return redirect(github_url)

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
