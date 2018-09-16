from .Member import Member
from enum import Enum, auto
from dataclasses import dataclass
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
