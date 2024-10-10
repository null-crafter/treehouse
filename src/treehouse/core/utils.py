import os
import typing as t
from collections import OrderedDict, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone

import frontmatter
import markdown
from slugify import slugify

loaded_data = defaultdict(dict)


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
    external_url: t.Optional[str] = None
    @property
    def is_external(self) -> bool:
        return bool(self.external_url)
    @property
    def unique_id(self) -> str:
        return self.filename

    @property
    def content(self) -> str:
        return markdown.markdown(
            self.markdown_content, extensions=["fenced_code", "codehilite"]
        )

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
            external_url=p.metadata.get("external_url")
        )
        if loaded_post.is_draft is False:
            loaded_data["posts"][loaded_post.slug] = loaded_post
            for c in loaded_post.categories:
                if c not in loaded_data["categories"]:
                    loaded_data["categories"][slugify(c)] = c
            for tag in loaded_post.tags:
                if tag not in loaded_data["tags"]:
                    loaded_data["tags"][slugify(tag)] = tag

        return loaded_post


def timestamp_from_datetime(dt: datetime) -> float:
    return dt.replace(tzinfo=timezone.utc).timestamp()


def sorted_dict(d: t.Mapping, *args, **kwargs) -> OrderedDict:
    return OrderedDict(sorted(d.items(), *args, **kwargs))
