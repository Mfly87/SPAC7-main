from ..absDataTypes import UniqueNamedData

class Category(UniqueNamedData):
    def __init__(self, id: str, name: str, description: str) -> None:
        super().__init__(id, name, description)
    
    def to_string(self) -> str:
        return " | ".join([
            self.id,
            self.name,
            self.description,
        ])