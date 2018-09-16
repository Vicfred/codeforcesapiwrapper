from .Problem import Problem
from .Party import Party
from enum import Enum, auto
from dataclasses import dataclass

@dataclass
class Submission:
    class Veredict(Enum):
        FAILED = auto()
        OK = auto()
        PARTIAL = auto()
        COMPILATION_ERROR = auto()
        RUNTIME_ERROR = auto()
        WRONG_ANSWER = auto()
        PRESENTATION_ERROR = auto()
        TIME_LIMIT_EXCEEDED = auto()
        MEMORY_LIMIT_EXCEEDED = auto()
        IDLENESS_LIMIT_EXCEEDED = auto()
        SECURITY_VIOLATED = auto()
        CRASHED = auto()
        INPUT_PREPARATION_CRASHED = auto()
        CHALLENGED = auto()
        SKIPPED = auto()
        TESTING = auto()
        REJECTED = auto()

    class Testset(Enum):
        SAMPLES = auto()
        PRETESTS = auto()
        TESTS = auto()
        CHALLENGES = auto()
        TESTSN = auto()

    id: int
    contestId: int
    creationTimeSeconds: int
    relativeTimeSeconds: int
    problem: Problem
    author: Party
    programmingLanguage: str
    veredict: Veredict
    testset: Testset
    passedTestCount: int
    timeConsumedMillis: int
    memoryConsumedBytes: int
