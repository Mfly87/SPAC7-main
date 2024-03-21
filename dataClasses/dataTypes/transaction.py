from ..absDataTypes import UniqueData

from datetime import datetime

from ..guardFunctions.str_func import str_non_empty
from ..guardFunctions.int_func import int_zero_or_greater
from ..guardFunctions.date_func import date_is_date


class Transaction(UniqueData):

    _product_id: str = None
    _date: datetime = None
    _quantity: int = None
    _type: str = None
    
    def __init__(self, id: str, product_id: str, date: str | datetime, quantity: int, type: str) -> None:
        super().__init__(id)
        
        self.product_id = product_id
        self.date = date
        self.quantity = quantity
        self.type = type
        
    
    @property
    def product_id(self) -> str:
        return self._product_id
    @product_id.setter
    def product_id(self, value) -> None:
        _value = str_non_empty(value)
        if _value is not None:
            self._product_id = _value

    @property
    def date(self) -> datetime:
        return self._date
    @date.setter
    def date(self, value) -> None:
        _value = date_is_date(value, self.date_format)
        if _value is not None:
            self._date = _value

    @property
    def quantity(self) -> int:
        return self._quantity
    @quantity.setter
    def quantity(self, value) -> None:
        _value = int_zero_or_greater(value)
        if _value is not None:
            self._quantity = _value

    @property
    def type(self) -> str:
        return self._type
    @type.setter
    def type(self, value) -> None:
        _value = str_non_empty(value)
        if _value is not None:
            self._type = _value

    @property
    def timestamp(self) -> str:
        if self._date is None:
            return None
        return self._date.strftime(self.date_format)

    def to_dict(self) -> dict[str,any]:
        return {
            "class": type(self).__name__,
            "id": self.id,
            "product_id": self.product_id,
            "date": self.timestamp,
            "type": self.type,
            "quantity": self.quantity,
        }

    def to_string(self) -> str:
        return " | ".join([
            self.id,
            self.product_id,
            self.timestamp,
            "Qty: " + str(self.quantity),
            self.type,
        ])