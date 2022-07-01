"""Super Basic flask Backend App"""
from model import ProjectManager
from flask import Flask, request
#domain stuff

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


