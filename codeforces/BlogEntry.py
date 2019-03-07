# -*- coding: utf-8 -*-
from dataclasses import dataclass, astuple
from typing import List


@dataclass
class BlogEntry:
    id: int
    originalLocale: str
    creationTimeSeconds: int
    authorHandle: str
    title: str
    locale: str
    modificationTimeSeconds: int
    allowViewHistory: bool
    tags: List[str]
    rating: int
    content: str = ""

    def __composite_values__(self):
        return astuple(self)
