# -*- coding: utf-8 -*-
from dataclasses import dataclass, astuple


@dataclass
class Member:
    handle: str

    def __composite_values__(self):
        return astuple(self)
