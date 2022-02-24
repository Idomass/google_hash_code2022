from dataset import Project

def find_employes_for_project(project, skills):
    for i, skill in enumerate(project.skills):
        wanted_skill_level = skill.level
        if project.mentors[i] == True:
            wanted_skill_level-=1

        if not (skill.name in skills.keys()):
            return False

        for level in skills[skill.name].keys():
            if level < wanted_skill_level:
                continue

            if len(skills[skill.name][level]) == 0:
                continue

            for employee in skills[skill.name][level]:
                if not employee.busy:
                    project.employees[i] = employee
                    break
            if project.employees[i] is None:
                continue

            # for employ in project.employees:
            #     employ_skills = employ.skills
            #     for j, skill_to_mentor in enumerate(project.skills):
            #         if skill_to_mentor.name == employ_skills[j].name \
            #             and employ_skills[j].level >= skill_to_mentor.level:
            #             project.mentors[j] = True
            break

        if project.employees[i] is None:
            return False

    return True
