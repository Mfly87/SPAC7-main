import abc

from datetime import datetime

class UniqueData(abc.ABC):
    def __init__(self, id : str) -> None:
        super().__init__()
        self._id = id
    
    @property
    def date_format(self) -> str:
        return "%Y-%m-%d"

    @property
    def id(self) -> str:
        return self._id
    
    @abc.abstractclassmethod
    def to_string(self) -> str:
        pass

    @abc.abstractclassmethod
    def to_dict(self) -> dict[str,str]:
        pass

    def matches_search(self, search_string : str) -> bool:
        if (search_string in self.id):
            return True
        return False
        
    def is_valid(self):
        _dict = self.__dict__
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