from typing import List
from dataset import Project


def max_proj_value(projects: List[Project]) -> int:
    """
    Returns the highest best_before + score project
    """
    return max(project.best_before + project.score - project.duration for project in projects)

def generate_output(projects: List[Project]):
    with open('output', 'w') as output:
        output.write(str(len(projects)) + '\n')

        for project in projects:
            output.write(str(project))
