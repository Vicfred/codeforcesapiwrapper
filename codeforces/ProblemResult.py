from enum import Enum, auto

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
