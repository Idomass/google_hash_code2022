from typing import List
from dataclasses import dataclass, field


@dataclass(order=True)
class Skill:
    def __init__(self, name: str, level: str):
        self.name = name
        self.level = int(level)

    name:   str = field(compare=False)
    level:  int


@dataclass(order=True)
class Employee:
    name:   str
    skills: List[Skill]

    @property
    def total_skill_level(self):
        return sum(skill.level for skill in self.skills)


@dataclass(order=True)
class Project:
    def __init__(self, name: str, duration: str, score: str, best_before: str, skills: List[Skill]) -> None:
        self.name           = name
        self.duration       = int(duration)
        self.score          = int(score)
        self.best_before    = int(best_before)
        self.skills         = skills

        # These are defaulted to None values, until changed
        self.employees      = [None] * len(skills)
        self.mentors        = [None] * len(skills)


    name:           str         = field(compare=False)
    duration:       int         = field(compare=False)
    score:          int
    best_before:    int         = field(compare=False)
    skills:         List[Skill] = field(compare=False)
    employees:      List[Employee]  = field(compare=False)
    mentors:        List[Employee]  = field(compare=False)
