from enum import Enum, auto

@dataclass
class Problem:
    class Type(Enum):
        PROGRAMMING = auto()
        QUESTION = auto()

    contestId: int
    problemsetName: str
    index: str
    name: str
    type: Type
    points: float
    tags: [str]
