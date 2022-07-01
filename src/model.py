

class Project:
    def __init__(self, name:str, id:str):
        self.name = name
        self.id = id

    def toString(self):
        main_string = f"| {self.name} |"
        line = "+" + (len(main_string) -2)*"-" + "+"
        return line + "\n" + main_string + "\n" + line

class ProjectManager:
    def __init__(self, projects:list=[]):
        self.projects = projects

    def add_project(self, name:str, id:str):
        if self.check_if_projects_exists(name):
            return False
        p = Project(name, id)
        self.projects.append(p)
        return True

    def remove_project(self, name:str):
        #get index of the project:
        delete_project = None
        for c, p in enumerate(self.projects):
            if p.name == name:
                delete_project = p
                break
        #remove from list:
        if delete_project:
            self.projects.remove(delete_project)
            return True
        return False

    def check_if_projects_exists(self, name:str):
        for pr in self.projects:
            if pr.name == name:
                return pr
        return False

    def print_out(self):
        for p in self.projects:
            print(p.toString())

    def list_of_dicts(self):
        return [vars(p) for p in self.projects]

    def rename_project(self, name:str, new_name:str):
        pr = self.check_if_projects_exists(name)
        if pr:
            pr.name = new_name
            return pr.name
        return False



