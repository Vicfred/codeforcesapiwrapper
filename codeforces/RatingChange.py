from dataclasses import dataclass


@dataclass
class RatingChange:
    contestId: int
    contestName: str
    handle: str
    rank: int
    ratingUpdateTimeSeconds: int
    oldRating: int
    newRating: int
