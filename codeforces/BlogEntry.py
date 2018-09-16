from dataclasses import dataclass
from typing import List


@dataclass
class BlogEntry:
    id: int
    originalLocale: str
    creationTimeSeconds: int
    authorHandle: str
    title: str
    content: str
    locale: str
    modificationTimeSeconds: int
    allowViewHistory: bool
    tags: List[str]
    rating: int
