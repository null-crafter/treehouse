import os

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        from core.utils import Post
        from django.conf import settings

        post_files = os.listdir(settings.POSTS_DIR)
        for f in post_files:
            Post.parse_file(settings.POSTS_DIR / f)
