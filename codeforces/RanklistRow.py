from .Party import Party
from .ProblemResult import ProblemResult
from dataclasses import dataclass
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
