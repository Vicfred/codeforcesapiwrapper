# -*- coding: utf-8 -*-
from enum import Enum, auto
from dataclasses import dataclass, astuple


@dataclass
class ProblemResult:
    class Type(Enum):
        PRELIMINARY = auto()
        FINAL = auto()

    points: float
    rejectedAttemptCount: int
    type: Type
    bestSubmissionTimeSeconds: int = -1  # This can be absent but it's not documented -__-
    penalty: int = -1  # This can be absent but it's not documented -__-

    def __post_init__(self):
        self.type = self.Type[self.type]

    def __composite_values__(self):
        return astuple(self)
