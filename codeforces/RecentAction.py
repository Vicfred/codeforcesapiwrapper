from .BlogEntry import BlogEntry
from .Comment import Comment
from dataclasses import dataclass


@dataclass
class RecentAction:
    timeSeconds: int
    blogEntry: BlogEntry
    comment: Comment
