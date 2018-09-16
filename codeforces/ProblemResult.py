from enum import Enum, auto
from dataclasses import dataclass


@dataclass
class ProblemResult:
    class Type(Enum):
        PRELIMINARY = auto()
        FINAL = auto()

    points: float
    penalty: int
    rejectedAttemptCount: int
    type: Type
    bestSubmissionTimeSeconds: int

    def __post_init__(self):
        self.type = self.Type[self.type]
