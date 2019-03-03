# -*- coding: utf-8 -*-

from .BlogEntry import BlogEntry
from .Comment import Comment
from dataclasses import dataclass


@dataclass
class RecentAction:
    timeSeconds: int
    blogEntry: BlogEntry = None
    comment: Comment = None

    def __post_init__(self):
        if self.blogEntry is not None:
            self.blogEntry = BlogEntry(**self.blogEntry)
        if self.comment is not None:
            self.comment = Comment(**self.comment)
