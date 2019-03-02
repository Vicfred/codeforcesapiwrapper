from .BlogEntry import BlogEntry
from .Comment import Comment
from dataclasses import dataclass


@dataclass
class RecentAction:
    timeSeconds: int
    blogEntry: BlogEntry = BlogEntry()  # TODO what should i do here? :s
    comment: Comment = Comment()
