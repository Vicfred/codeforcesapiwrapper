# -*- coding: utf-8 -*-
from .Party import Party
from .Problem import Problem
from enum import Enum, auto
from dataclasses import dataclass


@dataclass
class Hack:
    class Verdict(Enum):
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
    verdict: Verdict
    problem: Problem
    judgeProtocol: str  # TODO update to match specification using an object instead of a (json) string
    test: str = ""

    def __post_init__(self):
        self.verdict = self.Verdict[self.verdict]
        self.hacker = Party(**self.hacker)
        self.defender = Party(**self.defender)
        self.problem = Problem(**self.problem)
