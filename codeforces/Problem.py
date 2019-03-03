# -*- coding: utf-8 -*-
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
    problemSetName: str = ""
    points: float = -1.0
    rating: int = -1

    def __post_init__(self):
        self.type = self.Type[self.type]
