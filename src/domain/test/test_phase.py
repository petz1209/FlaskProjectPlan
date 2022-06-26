from src.domain.phase import Phase
from src.domain.workpackage import WorkPackage

def test_create_phase_no_position(name:str=None):
    if not name: name = "Phase 1"
    phase = Phase(name=name)
    assert phase.name == name
    assert phase.position is None
    assert phase.packages is None
    return phase

def test_create_phase_with_position(name:str=None, position:int=None):
    if not name: name = "Phase 1"
    if not position: position = 4
    phase = Phase(name=name, position=position)
    assert phase.name == name
    assert phase.position == position
    assert phase.packages is None
    return phase

def test_add_packages_to_phase():
    """Tests the adding capabilities of Phase"""
    phase = test_create_phase_with_position(name="Phase 1", position=1)
    workpackage_list = [WorkPackage(name="WP 1"),
                        WorkPackage(name="WP 2"),
                        WorkPackage(name="WP 3"),
                        WorkPackage(name="WP 4"),
                        WorkPackage(name="WP 5", _is_milestone=True)
                        ]

    for w in workpackage_list:
        phase.add_package(w)
    assert phase.packages[4].name == "WP 5"
    return phase

def test_add_package_at_some_position_of_phases():
    """Tests add_package at spezific position"""
    phase = test_add_packages_to_phase()
    wp = WorkPackage(name="Disruptor")
    phase.add_package(wp, position=4)
    assert phase.packages[4].name == "Disruptor"
    assert phase.packages[5].name == "WP 5"
    return phase
