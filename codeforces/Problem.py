from enum import Enum, auto
from dataclasses import dataclass
from typing import List


@dataclass
class Problem:
    class Type(Enum):
        PROGRAMMING = auto()
        QUESTION = auto()

    index: str
    name: str
    type: Type
    tags: List[str]
    contestId: int = -1
    problemsetName: str = ""
    points: float = -1.0
