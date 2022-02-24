from typing import List
from dataclasses import dataclass


@dataclass
class Skill:
    def __init__(self, name: str, level: str):
        self.name = name
        self.level = int(level)

    name:   str
    level:  int


@dataclass
class Employee:
    name:   str
    skills: List[Skill]


@dataclass
class Project:
    def __init__(self, name: str, duration: str, score: str, best_before: str, skills: List[Skill]) -> None:
        self.name           = name
        self.duration       = int(duration)
        self.score          = int(score)
        self.best_before    = int(best_before)
        self.skills         = skills

    name:           str
    duration:       int
    score:          int
    best_before:    int
    skills:         List[Skill]
