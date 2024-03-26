import abc
from datetime import datetime

from ..guardFunctions.str_func import str_non_empty

class UniqueData(abc.ABC):

    _id : str = None

    def __init__(self, id : str) -> None:
        super().__init__()

        _value = str_non_empty(id)
        if _value is not None:
            self._id = _value

    @property
    def date_format(self) -> str:
        return "%Y-%m-%d"

    @property
    def id(self) -> str:
        return self._id
    @id.setter
    def id(self, value) -> None:
        '''This parameter can not be changed, but is still exposed to prevent generic functions from crashing'''
        pass
    
    @abc.abstractmethod
    def to_string(self) -> str:
        pass
    
    @abc.abstractmethod
    def to_list(self) -> list[any]:
        pass

    @abc.abstractclassmethod
    def get_headers() -> list[str]:
        pass
    
    @abc.abstractclassmethod
    def get_types() -> list[type]:
        pass

    def to_dict(self) -> dict[str,any]:
        return dict(zip(self.get_headers(), self.to_list()))

    @classmethod
    def get_dependencies(self) -> list[str]:
        '''Returns a list of class names required to build this class'''
        _dependency_list = []
        for _header in self.get_headers():
            _split = _header.split("_")
            if len(_split) != 2:
                continue
            if _split[1].lower() != "id":
                continue
            _dependency_list.append(_split[0])
        return _dependency_list

    def is_valid(self):
        '''Returns False if any parameters have not been set'''
        _dict = self.to_dict()
        for _value in _dict.values():
            if _value is None:
                return False
        return True
    
    def __eq__(self, __value: object) -> bool:
        '''Ensures the equal opperator functions based on class content'''

        if not isinstance(__value, type(self)):
            return False
        
        _list_a = self.to_list()
        _list_b = __value.to_list()

        for a, b in zip(_list_a, _list_b):
            if a != b:
                return False
            
        return True