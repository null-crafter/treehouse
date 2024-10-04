import typing as t
from slugify import slugify
import os
from dataclasses import dataclass, replace
from datetime import datetime
import markdown

import frontmatter

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
            is_draft=p.metadata["draft"],
            categories=p.metadata["categories"],
            tags=p.metadata["tags"],
            markdown_content=p.content,
        )
        loaded_posts[loaded_post.slug] = loaded_post
        return loaded_post
