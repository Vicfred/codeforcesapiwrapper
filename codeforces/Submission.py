# -*- coding: utf-8 -*-
from .Problem import Problem
from .Party import Party
from enum import Enum, auto
from dataclasses import dataclass, astuple


@dataclass
class Submission:
    class Verdict(Enum):
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

    class TestSet(Enum):
        SAMPLES = auto()
        PRETESTS = auto()
        TESTS = auto()
        CHALLENGES = auto()
        TESTSN = auto()

    id: int
    creationTimeSeconds: int
    relativeTimeSeconds: int
    problem: Problem
    author: Party
    programmingLanguage: str
    verdict: Verdict
    testset: TestSet
    passedTestCount: int
    timeConsumedMillis: int
    memoryConsumedBytes: int
    contestId: int = -1

    def __post_init__(self):
        self.problem = Problem(**self.problem)
        self.author = Party(**self.author)
        self.verdict = self.Verdict[self.verdict]
        self.testset = self.TestSet[self.testset]

    def __composite_values__(self):
        return astuple(self)
