from .Member import Member
from enum import Enum, auto

@dataclass
class Party:
    class ParticipantType(Enum):
        CONTESTANT = auto()
        PRACTICE = auto()
        VIRTUAL = auto()
        MANAGER = auto()
        OUT_OF_COMPETITION = auto()

    contestId: int
    members: [Member]
    participantType: ParticipantType
    teamId: int
    teamName: str
    ghost: bool
    room: int
    startTimeSeconds: int
