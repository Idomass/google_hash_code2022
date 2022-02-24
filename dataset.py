from typing import List
from dataclasses import dataclass


@dataclass
class Skill:
    name:   str
    level:  int


@dataclass
class Employee:
    name:   str
    skills: List[Skill]


@dataclass
class Project:
    name:           str
    duration:       int
    score:          int
    best_before:    int
    required_roles: List[Skill]
