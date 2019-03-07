# -*- coding: utf-8 -*-
from dataclasses import dataclass, astuple


@dataclass
class ProblemStatistics:
    index: str
    solvedCount: int
    contestId: int = -1

    def __composite_values__(self):
        return astuple(self)
