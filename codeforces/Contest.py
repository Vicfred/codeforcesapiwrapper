from enum import Enum, auto
from dataclasses import dataclass


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
    startTimeSeconds: int = -1
    relativeTimeSeconds: int = -1
    preparedBy: str = ""
    websiteUrl: str = ""
    description: str = ""
    difficulty: int = -1
    kind: str = ""
    icpcRegion: str = ""
    country: str = ""
    city: str = ""
    season: str = ""

    def __post_init__(self):
        self.type = self.Type[self.type]
        self.phase = self.Phase[self.phase]
