from dataclasses import dataclass


@dataclass
class ProblemStatistics:
    index: str
    solvedCount: int
    contestId: int = -1
