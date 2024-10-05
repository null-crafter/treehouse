import os
import typing as t
from dataclasses import dataclass, replace, field
from datetime import datetime

import frontmatter
import markdown
from slugify import slugify

loaded_posts = {}


@dataclass
class Post:
    filename: str
    title: str
    date: datetime
    markdown_content: str
    categories: t.List[str]
    tags: t.List[str]
    is_draft: bool
    author: str = field(default="Hare")

    @property
    def unique_id(self) -> str:
        return self.filename

    @property
    def content(self) -> str:
        return markdown.markdown(self.markdown_content, extensions=["fenced_code"])

    @property
    def slug(self) -> str:
        return slugify(os.path.splitext(self.filename)[0])

    @classmethod
    def parse_file(cls, path) -> "Post":
        p = frontmatter.load(path)
        loaded_post = Post(
            filename=os.path.basename(path),
            title=p.metadata["title"],
            date=p.metadata["date"],
            is_draft=p.metadata.get("draft", False),
            categories=p.metadata.get("categories", []),
            tags=p.metadata.get("tags", []),
            author=p.metadata.get("author", "Hare"),
            markdown_content=p.content,
        )
        if loaded_post.is_draft is False:
            loaded_posts[loaded_post.slug] = loaded_post
        return loaded_post
