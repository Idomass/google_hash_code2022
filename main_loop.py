import argparse

from typing import List, Tuple
from venv import create
from dataset import Skill, Employee, Project
from find_employes import find_employes_for_project
from program import create_multi_dict
from analyze import max_proj_value, generate_output

def progress_day(ongoing_projects, completed_projects, working_employees):
    projects_done_today = []
    for project in ongoing_projects:
        project.duration -= 1
        if project.duration == 0:
            completed_projects.append(project)
            projects_done_today.append(project)
            for i, employee in enumerate(project.employees):
                for skill in employee.skills:
                    if project.skills[i].name == skill.name:
                        if project.skills[i].level >= skill.level:
                            skill.level +=1
                employee.busy = False
                working_employees.remove(employee)
    for project in projects_done_today:
        ongoing_projects.remove(project)

def main_loop(employees: List[Employee], projects: List[Project]):
    skills = create_multi_dict(projects, employees)
    ongoing_projects = []
    working_employees = []
    completed_projects = []
    curr_day = 0
    max_day = max_proj_value(projects)
    print(max_day)
    for i in range(max_day):
        if all([employee.busy for employee in employees]):
            curr_day += 1
            progress_day(ongoing_projects, completed_projects, working_employees)
            continue
        projects = [project for project in projects if project not in ongoing_projects and project not in completed_projects]
        projects = [project for project in projects if project.best_before + project.score - project.duration > curr_day]

        for project in projects:
            if find_employes_for_project(project, skills):
                ongoing_projects.append(project)
                for employee in project.employees:
                    assert employee.busy == False
                    employee.busy = True
                    working_employees.append(employee)

        curr_day += 1
        progress_day(ongoing_projects, completed_projects, working_employees)

    generate_output(completed_projects + ongoing_projects)
