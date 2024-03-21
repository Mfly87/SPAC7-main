import abc
import re
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
    def id(self, value) -> str:
        _value = str_non_empty(value)
        if _value is not None:
            self._id = _value
    
    @abc.abstractclassmethod
    def to_string(self) -> str:
        pass

    @abc.abstractclassmethod
    def to_dict(self) -> dict[str,str]:
        pass

    def matches_search(self, search_string : str) -> bool:
        print(search_string)
        print(self.id)
        print(re.search(search_string, self.id, re.IGNORECASE))
        if re.search(search_string, self.id, re.IGNORECASE):
            return True
        return False
        
    def is_valid(self):
        _dict = self.to_dict()
        for _value in _dict.values():
            if _value is None:
                return False
        return True
    





    def _print_error(self, exception : Exception) -> None:
        template = "   An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(exception).__name__, exception.args)
        print( message )

    def _convert_to_int_or_none(self, value : any) -> int | None:
        if isinstance(value, str):
            try:
                value = int(value)
            except ValueError as ex:
                self._print_error(ex)
                return
        if isinstance(value, int):
            return value
        return None
    
    def _convert_to_datetime_or_none(self, value : any) -> datetime | None:
        if isinstance(value, str):
            try:
                value = datetime.strftime(value, self.date_format)
            except ValueError as ex:
                self._print_error(ex)
                return
        if isinstance(value, datetime):
            return value
        return None