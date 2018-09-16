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
    tags: [str]
    rating: int
