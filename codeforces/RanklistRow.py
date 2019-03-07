# -*- coding: utf-8 -*-
from .Party import Party
from .ProblemResult import ProblemResult
from dataclasses import dataclass, astuple
from typing import List


@dataclass
class RanklistRow:
    party: Party
    rank: int
    points: float
    penalty: int
    successfulHackCount: int
    unsuccessfulHackCount: int
    problemResults: List[ProblemResult]
    lastSubmissionTimeSeconds: int = -1

    def __post_init__(self):
        self.party = Party(**self.party)

        problemResults = []
        for problemResult in self.problemResults:
            problemResults.append(ProblemResult(**problemResult))
        self.problemResults = problemResults

    def __composite_values__(self):
        return astuple(self)
