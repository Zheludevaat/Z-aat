from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Card:
    id: int
    name: str
    triad: Tuple[str, str, str]
    path: int
    letter: str
    astro: str
    alch: str
    cycle: str
    geom: List[str]
    motifs: List[str]


@dataclass
class Motif:
    code: str
    description: str
