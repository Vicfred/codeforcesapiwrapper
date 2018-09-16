from enum import Enum, auto

@dataclass
class Contest:
    class Type(Enum):
        CF = auto()
        IOI = auto()
        ICPC = auto()

    class Phase(Enum):
        BEFORE = auto()
        CODING = auto()
        PENDING_SYSTEM_TEST = auto()
        SYSTEM_TEST = auto()
        FINISHED = auto()

    id: int
    name: str
    type: Type
    phase: Phase
    frozen: bool
    durationSeconds: int
    startTimeSeconds: int
    relativeTimeSeconds: int
    preparedBy: str
    websiteUrl: str
    description: str
    difficulty: int
    kind: str
    icpcRegion: str
    country: str
    city: str
    season: str
