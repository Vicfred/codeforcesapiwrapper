# -*- coding: utf-8 -*-
from dataclasses import dataclass, astuple


@dataclass
class RatingChange:
    contestId: int
    contestName: str
    handle: str
    rank: int
    ratingUpdateTimeSeconds: int
    oldRating: int
    newRating: int

    def __composite_values__(self):
        return astuple(self)
