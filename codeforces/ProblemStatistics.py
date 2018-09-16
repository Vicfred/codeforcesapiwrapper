from dataclasses import dataclass


@dataclass
class ProblemStatistics:
    contestId: int
    index: str
    solvedCount: int
