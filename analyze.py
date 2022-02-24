from typing import List
from dataset import Project


def max_proj_value(projects: List[Project]) -> int:
    """
    Returns the highest best_before + score project
    """

    highest_value = 0
    selected_index = 0
    for index, project in enumerate(projects):
        if project.best_before + project.score - project.duration > highest_value:
            highest_value = project.best_before + project.score - project.duration
            selected_index = index

    return selected_index
