# -*- coding: utf-8 -*-
from .Member import Member
from enum import Enum, auto
from dataclasses import dataclass, astuple
from typing import List


@dataclass
class Party:
    class ParticipantType(Enum):
        CONTESTANT = auto()
        PRACTICE = auto()
        VIRTUAL = auto()
        MANAGER = auto()
        OUT_OF_COMPETITION = auto()

    members: List[Member]
    participantType: ParticipantType
    ghost: bool
    contestId: int = -1
    teamId: int = -1
    teamName: str = ""
    room: int = -1
    startTimeSeconds: int = -1

    def __post_init__(self):
        self.participantType = self.ParticipantType[self.participantType]

        members = []
        for member in self.members:
            members.append(Member(**member))
        self.members = members

    def __composite_values__(self):
        return astuple(self)
