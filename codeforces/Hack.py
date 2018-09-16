from .Party import Party
from .Problem import Problem
from enum import Enum, auto
from dataclasses import dataclass


@dataclass
class Hack:
    class Veredict(Enum):
        HACK_SUCCESSFUL = auto()
        HACK_UNSUCCESSFUL = auto()
        INVALID_INPUT = auto()
        GENERATOR_INCOMPILABLE = auto()
        GENERATOR_CRASHED = auto()
        IGNORED = auto()
        TESTING = auto()
        OTHER = auto()

    id: int
    creationTimeSeconds: int
    hacker: Party
    defender: Party
    veredict: Veredict
    problem: Problem
    test: str
    judgeProtocol: str  # TODO update to match specification
