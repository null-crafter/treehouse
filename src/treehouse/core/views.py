import os
from datetime import timezone

from core.utils import Post, loaded_data, timestamp_from_datetime
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.templatetags.static import static
from slugify import slugify


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
    posts = loaded_data["posts"].values()
    tags = set()
    categories = set()
    for p in posts:
        categories = categories.union(set(p.categories))
        tags = tags.union(set(p.tags))
    tags = {slugify(tag): tag for tag in sorted(list(tags))}
    categories = {slugify(c): c for c in sorted(list(categories))}
    return render(
        request,
        "core/posts.html",
        {
            "posts": sorted(
                loaded_data["posts"].values(),
                key=lambda p: -timestamp_from_datetime(p.date),
            ),
            "tags": tags,
            "categories": categories,
        },
    )


def category(request, slug: str):
    if not slug in loaded_data["categories"]:
        raise Http404()
    category = loaded_data["categories"][slug]
    posts = sorted(
        filter(
            lambda p: category in p.categories,
            loaded_data["posts"].values(),
        ),
        key=lambda p: -timestamp_from_datetime(p.date),
    )
    if not posts:
        raise Http404()
    return render(request, "core/category.html", {"posts": posts, "category": category})


def tag(request, slug: str):
    if not slug in loaded_data["tags"]:
        raise Http404()
    tag = loaded_data["tags"][slug]
    posts = sorted(
        filter(
            lambda p: tag in p.tags,
            loaded_data["posts"].values(),
        ),
        key=lambda p: -timestamp_from_datetime(p.date),
    )
    if not posts:
        raise Http404()
    return render(request, "core/tag.html", {"posts": posts, "tag": tag})

        
def post_single(request, slug: str):
    post = loaded_data["posts"].get(slug)
    if post is None:
        raise Http404()
    return render(request, "core/post_single.html", {"post": post})
