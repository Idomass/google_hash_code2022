from typing import List
from dataclasses import dataclass

@dataclass
class Project:
    name:           str
    duration:       int
    score:          int
    best_before:    int
    required_roles: List
