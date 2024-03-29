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
    def name(self, value) -> None:
        _value = str_non_empty(value)
        if _value is not None:
            self._name = _value
    
    @property
    def description(self) -> str:
        return self._description
    @description.setter
    def description(self, value) -> None:
        _value = str_non_empty(value)
        if _value is not None:
            self._description = _value