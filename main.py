#! /usr/bin/env python3

import argparse

from typing import List, Tuple
from dataset import Skill, Employee, Project
from main_loop import main_loop

def parse_data(file) -> Tuple[List[Employee], List[Project]]:
    """
    Returns a list of avialable employees and projects
    """

    num_employee, num_projects = (int(x) for x in file.readline().strip('\n').split())

    employees   = []
    projects    = []
    for _ in range(num_employee):
        name, num_skills = file.readline().split()

        skills = [Skill(*file.readline().split()) for _ in range(int(num_skills))]

        employees.append(Employee(name, skills, False))

    for _ in range(num_projects):
        project_line = file.readline().split()
        num_skills = int(project_line[4])

        skills = [Skill(*file.readline().split()) for _ in range(int(num_skills))]

        projects.append(Project(*project_line[:4], skills))

    return employees, projects

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=argparse.FileType('r'))

    return parser.parse_args()


def main():
    args = parse_args()
    employees, projects = parse_data(args.filename)
    main_loop(employees, projects)




if __name__ == '__main__':
    main()
