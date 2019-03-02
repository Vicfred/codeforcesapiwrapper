from .BlogEntry import BlogEntry
from .Comment import Comment
from dataclasses import dataclass


@dataclass
class RecentAction:
    timeSeconds: int
    blogEntry: BlogEntry# = BlogEntry()  # TODO what should i do here? :s, still needs testing
    comment: Comment# = Comment()

    def __post_init__(self):
        self.blogEntry = BlogEntry(**self.blogEntry)
        self.comment = Comment(**self.comment)
