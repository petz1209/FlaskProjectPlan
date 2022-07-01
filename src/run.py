"""Super Basic flask Backend App"""

from flask import Flask, request
#domain stuff
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

    def remove_projects(self, name:str):
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
                return True
        return False

    def print_out(self):
        for p in self.projects:
            print(p.toString())

    def list_of_dicts(self):
        return [vars(p) for p in self.projects]

app = Flask(__name__)

@app.route("/project", methods=["POST"])
def add_project():
    state = project_manager.add_project(name=request.json["name"], id=request.json["id"])
    project_manager.print_out()
    if state:
        return {"status": "ok", "message": "project created"}
    return {"status": "error", "message": "project allready exists"}


@app.route("/projects")
def get_all_projects():
    return {"status": "ok", "data": project_manager.list_of_dicts()}



if __name__ == '__main__':

    project_manager = ProjectManager()
    port = 3000
    app.run(host="0.0.0.0", port=port, debug=True)


