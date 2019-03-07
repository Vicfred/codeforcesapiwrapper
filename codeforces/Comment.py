# -*- coding: utf-8 -*-
from dataclasses import dataclass, astuple


@dataclass
class Comment:
    id: int
    creationTimeSeconds: int
    commentatorHandle: str
    locale: str
    text: str
    rating: int
    parentCommentId: int = -1

    def __composite_values__(self):
        return astuple(self)
