"""Only Flask Endpoint Domain handled in models.py"""
from model import ProjectManager
from flask import Flask, request


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

@app.route("/project", methods=["DELETE"])
def delete_project():
    project_manager.remove_project(name=request.args["name"])
    return {"status": "ok", "message": f"project {request.args['name']} is deleted"}

@app.route("/project", methods=["PUT"])
def rename_project():
    nn = project_manager.rename_project(name=request.args["name"], new_name=request.args["new_name"])
    if nn:
        return {"status": "ok", "message": f"project {request.args['name']} has been changed to {nn}"}
    else:
        return {"status": "error", "message": f"project {request.args['name']} could not be renamed"}

if __name__ == '__main__':

    project_manager = ProjectManager()
    port = 3000
    app.run(host="0.0.0.0", port=port, debug=True)


