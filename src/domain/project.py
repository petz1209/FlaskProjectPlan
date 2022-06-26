import uuid
from typing import Optional, List
from dataclasses import dataclass
from src.domain.phase import Phase

@dataclass
class Project:
    id = str(uuid.uuid4())
    name: str
    description: Optional[str] = None
    phases: Optional[List[Phase]] = None

    def add_phase(self, phase:Phase):
        if not self.phases:
            phase.position = 0
            self.phases = [phase]
            return
        if not phase.position:
            phase.position = len(self.phases)
        self.phases.append(phase)
        return

    def get_phase(self, name):
        if not self.phases:
            return "No Phases yet"
        for ps in self.phases:
            if ps.name == name:
                return ps

    def to_string(self):
        string_rep = f"{self.name}"
        if self.phases:
            for ps in self.phases:
                string_rep += "\n\t" + ps.to_string()
        return string_rep

