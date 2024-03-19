from .unique_data import UniqueData

class UniqueNamedData(UniqueData):
    def __init__(self, id: str, name : str, description : str) -> None:
        super().__init__(id)

        self._name = name
        self._description = description
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def description(self) -> str:
        return self._description

    def matches_search(self, search_string : str) -> bool:
        if super().matches_search(search_string):
            return True
        if (search_string in self.name):
            return True
        if (search_string in self.description):
            return True
        return False