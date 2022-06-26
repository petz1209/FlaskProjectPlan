import uuid
from typing import Optional, List
from dataclasses import dataclass
from src.domain.workpackage import WorkPackage

@dataclass
class Phase:
    id = str(uuid.uuid4())
    name: str
    position: Optional[int] = None
    packages: Optional[List[WorkPackage]] = None

    def to_string(self):
        string_rep = f"{self.position+1}. {self.name}"
        if self.packages:
            for p in self.packages:
                string_rep += f"\n\t\t{self.position+1}.{p.to_string()}"
        return string_rep

    def add_package(self,package, position:int = None):
        if not self.packages:
            package.position = 0
            self.packages = [package]
            return
        if not position or position < 0 or position > len(self.packages):
            package.position = len(self.packages)
            self.packages.append(package)
            return
        package.position = position
        for x in self.packages:
            if x.position >= position:
                x.position += 1
        self.packages.insert(position, package)
