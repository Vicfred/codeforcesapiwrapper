from .BlogEntry import BlogEntry
from .Comment import Comment

@dataclass
class RecentAction:
    timeSeconds: int
    blogEntry: BlogEntry
    comment: Comment
