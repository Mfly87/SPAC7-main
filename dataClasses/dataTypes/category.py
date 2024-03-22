from ..absDataTypes import UniqueNamedData

class Category(UniqueNamedData):
    def __init__(self, id: str, name: str, description: str) -> None:
        super().__init__(id, name, description)
    
    def to_dict(self) -> dict[str,any]:
        return {
            "class": type(self).__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }

    def to_string(self) -> str:
        return " | ".join(self.to_list())
    
    def to_list(self) -> list[any]:
        return [
            self.id,
            self.name,
            self.description,
        ]
    
    @staticmethod
    def get_headers() -> list[str]:
        return [
            "id",
            "name",
            "description",
        ]