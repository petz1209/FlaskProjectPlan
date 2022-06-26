import uuid
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class WorkPackage:
    id = str(uuid.uuid4())
    name: str
    position: Optional[int] = None
    _is_milestone: Optional[bool] = False
    def to_string(self):
        string_rep = f"{self.position+1}. {self.name}"
        if self._is_milestone:
            string_rep += " #"
        return string_rep