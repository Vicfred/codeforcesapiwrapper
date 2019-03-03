# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class User:
    handle: str
    contribution: int
    rank: str
    rating: int
    maxRank: str
    maxRating: int
    lastOnlineTimeSeconds: int
    registrationTimeSeconds: int
    friendOfCount: int
    avatar: str
    titlePhoto: str
    email: str = ""
    vkId: str = ""
    openId: str = ""
    firstName: str = ""
    lastName: str = ""
    country: str = ""
    city: str = ""
    organization: str = ""
