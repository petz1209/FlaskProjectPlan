from src.domain.project import Project
from src.domain.phase import Phase
#unittests for Project

def test_create_project_basic():
    project = Project(name="TestProject", description="This is a TestProject")
    assert project.name == "TestProject"
    assert project.description == "This is a TestProject"
    assert id is not None
    assert project.phases is None
    return project

def test_add_phases_to_project():
    project = test_create_project_basic()
    phase_list = [Phase(name="Phase 1"), Phase(name="Phase 2"), Phase(name="Phase 3")]
    for phase in phase_list:
        project.add_phase(phase)
    assert project.phases != None
    assert project.phases[0].name == "Phase 1"
    return project





