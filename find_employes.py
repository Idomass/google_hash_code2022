from dataset import Project

def find_employes_for_project(project, skills):
    for i, skill in enumerate(project.skills):
        wanted_skill_level = skill.level
        if mentors[i] == True:
            wanted_skill_level-=1
        
        if not (skill.name in skills.keys()):
            return False

        for level in skills[skill.name].keys:
            if level < wanted_skill_level:
                continue

            if len(skills[skill.name][level]) == 0:
                continue

            employee = skills[skill.name][level][0]
            project.employees[i] = employee

            for employ_skill in employees.skills:
                for j, skill_to_mentor in enumerate(project.skills):
                    if skill_to_mentor.name == employ_skill.name \
                        and employ_skill.level >= skill_to_mentor.level:
                        project.mentors[j] = True
            break

        return True

    return False
