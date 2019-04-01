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
        TESTS1 = auto()
        TESTS2 = auto()
        TESTS3 = auto()
        TESTS4 = auto()
        TESTS5 = auto()
        TESTS6 = auto()
        TESTS7 = auto()
        TESTS8 = auto()
        TESTS9 = auto()

    id: int
    creationTimeSeconds: int
    relativeTimeSeconds: int
    problem: Problem
    author: Party
    programmingLanguage: str
    testset: TestSet
    passedTestCount: int
    timeConsumedMillis: int
    memoryConsumedBytes: int
    contestId: int = -1
    verdict: Verdict = None

    def __post_init__(self):
        self.problem = Problem(**self.problem)
        self.author = Party(**self.author)
        self.testset = self.TestSet[self.testset]
        if self.verdict is not None:
            self.verdict = self.Verdict[self.verdict]

    def __composite_values__(self):
        return astuple(self)
