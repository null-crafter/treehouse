from core import views
from django.urls import path

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("favicon.ico", views.favicon, name="favicon"),
    path("about/", views.about, name="about"),
    path("posts/", views.post_list, name="posts"),
    path("post/<slug:slug>/", views.post_single, name="post"),
]
