import pytest
from model import ProjectManager
def test_addProject():
    name="Testname"
    id="testid"
    project_manager = ProjectManager()
    project_manager.add_project(name=name, id=id)
    assert project_manager.list_of_dicts() == [{"name": name, "id": id}]

