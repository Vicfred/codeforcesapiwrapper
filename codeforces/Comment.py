from dataclasses import dataclass


@dataclass
class Comment:
    id: int
    creationTimeSeconds: int
    commentatorHandle: str
    locale: str
    text: str
    parentCommentId: int
    rating: int
