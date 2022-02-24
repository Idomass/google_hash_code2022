from dataset import Project

def find_employes_for_project(project, skills):
    for i, skill in emulate(project.skills):
        wanted_skill_level = skill.level
        if mentors[i] == True:
            wanted_skill_level-=1

        if len(skills[skill.name][wanted_skill_level]) == 0:
            return False

        employee = skills[skill.name][wanted_skill_level][0]
        project.employees[i] = employee

        for employ_skill in employees.skills:
            for j, skill_to_mentor in emulate(project.skills):
                if skill_to_mentor.name == employ_skill.name \
                    and employ_skill.level >= skill_to_mentor.level
                    project.mentors[j] = True
    return True