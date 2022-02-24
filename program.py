from typing import List
from dataset import Project, Skill, Employee


def create_relevant_skills(projects: List[Project]) -> List[str]:
    relevant_skills = {}
    for project in projects:
        for skill in project.skills:
            relevant_skills[skill.name] = {}

    return relevant_skills

# def AddEmloyeeToSkillList(skillsDict, skill: Skill, emloyee: Employee):
#     emloyee_level = skill.level
#     if emloyee_level in skillsDict[skill.name]:
#         existing_emloyies = skillsDict[skill.name][emloyee_level]
#         skillsDict[skill.name][emloyee_level]  = [emloyee] + existing_emloyies
#     else:
#         skillsDict[skill.name][emloyee_level]  = [emloyee]    

def create_multi_dict(projects: List[Project], employees : List[Employee]):
    skill_dict = create_relevant_skills(projects)

    for emloyee in employees:
        for skill in emloyee.skills:
            if skill.name in skill_dict:
                if skill.level not in skill_dict[skill.name]:
                    skill_dict[skill.name][skill.level] = []

                skill_dict[skill.name][skill.level] += [emloyee]
                
    return skill_dict
