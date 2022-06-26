"""Testing Domain interaction"""
from src.domain.project import Project
from src.domain.phase import Phase
from src.domain.workpackage import WorkPackage

def test_create_project():
    project = Project(name="TestProject", description="This is a TestProject")
    assert project.name == "TestProject"
    return project


def test_create_phase(name:str=None, position:int=None):
    if not name: name="Testphase"
    if not position: position= 1
    phase = Phase(name=name, position=position)
    assert phase.name == name
    assert phase.position == position
    return phase

def add_workpackages_to_phase():
    phase = test_create_phase(name="Phase 1")
    workpackage_list = [WorkPackage(name="WP 1"),
                        WorkPackage(name="WP 2"),
                        WorkPackage(name="WP 3"),
                        WorkPackage(name="WP 4"),
                        WorkPackage(name="WP 5", _is_milestone=True)
                        ]
    for w in workpackage_list:
        phase.add_package(w)
    assert phase.packages[4].name == "WP 5"

    wp = WorkPackage(name="Disruptor")
    phase.add_package(wp, position=4)
    assert phase.packages[4].name == "Disruptor"
    assert phase.packages[5].name == "WP 5"





def test_add_phases_to_project():
    phase_list = [Phase(name="Phase 1"), Phase(name="Phase 2"), Phase(name="Phase 3")]
    project = test_create_project()
    for phase in phase_list:
        project.add_phase(phase)
    assert project.phases != None
    assert project.phases[0].name == "Phase 1"
    return project

def test_project_refernces():
    workpackage_list = [WorkPackage(name="WP 1"),
                        WorkPackage(name="WP 2"),
                        WorkPackage(name="WP 3"),
                        WorkPackage(name="WP 4"),
                        WorkPackage(name="WP 5", _is_milestone=True)
                        ]
    project = test_add_phases_to_project()
    for phase in project.phases:
        for w in workpackage_list:
            phase.add_package(w)
    assert project != None

    return project


def test_set_workpackage_on_position_in_phase():
    phase = test_create_phase()






