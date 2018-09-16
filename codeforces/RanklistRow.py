from .Party import Party
from .ProblemResult import ProblemResult
from dataclasses import dataclass


@dataclass
class RanklistRow:
    party: Party
    rank: int
    points: float
    penalty: int
    successfulHackCount: int
    unsuccessfulHackCount: int
    problemResults: [ProblemResult]
    lastSubmissionTimeSeconds: int
