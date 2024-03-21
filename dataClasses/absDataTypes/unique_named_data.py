from .unique_data import UniqueData
from ..guardFunctions.str_func import str_non_empty

import re

class UniqueNamedData(UniqueData):

    _name: str = None
    _description: str = None

    def __init__(self, id: str, name : str, description : str) -> None:
        super().__init__(id)

        self.name = name
        self.description = description
    
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value) -> str:
        _value = str_non_empty(value)
        if _value is not None:
            self._name = _value
    
    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, value) -> str:
        _value = str_non_empty(value)
        if _value is not None:
            self._description = _value

    def matches_search(self, search_string : str) -> bool:
        if super().matches_search(search_string):
            return True
        if re.search(search_string, self.name, re.IGNORECASE):
            return True
        if re.search(search_string, self.description, re.IGNORECASE):
            return True
        return False