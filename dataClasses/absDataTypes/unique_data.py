import abc
from datetime import datetime

from ..guardFunctions.str_func import str_non_empty

class UniqueData(abc.ABC):

    _id : str = None

    def __init__(self, id : str) -> None:
        super().__init__()
        self.id = id

    @property
    def date_format(self) -> str:
        return "%Y-%m-%d"

    @property
    def id(self) -> str:
        return self._id
    @id.setter
    def id(self, value) -> None:
        _value = str_non_empty(value)
        if _value is not None:
            self._id = _value
    
    @abc.abstractclassmethod
    def to_string(self) -> str:
        pass
    
    @abc.abstractclassmethod
    def to_list(self) -> list[any]:
        pass

    @abc.abstractstaticmethod
    def get_headers() -> list[str]:
        pass

    def to_dict(self) -> dict[str,any]:
        return dict(zip(self.get_headers(), self.to_list()))


    def is_valid(self):
        _dict = self.to_dict()
        for _value in _dict.values():
            if _value is None:
                return False
        return True
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, type(self)):
            return False
        
        _list_a = self.to_list()
        _list_b = __value.to_list()

        for a, b in zip(_list_a, _list_b):
            if a != b:
                return False
            
        return True