from .unique_data import UniqueData

import re

class UniqueNamedData(UniqueData):
    def __init__(self, id: str, name : str, description : str) -> None:
        super().__init__(id)

        self._name = name
        self._description = description
    
    @property
    def name(self) -> str:
        return self._name
    
    def change_name(self, name : str) -> None:
        self._name = name

    def change_description(self, description : str) -> None:
        self._description = description

    @property
    def description(self) -> str:
        return self._description

    def matches_search(self, search_string : str) -> bool:
        if super().matches_search(search_string):
            return True
        if re.search(search_string, self.name, re.IGNORECASE):
            return True
        if re.search(search_string, self.description, re.IGNORECASE):
            return True
        return False