from ..absDataTypes import UniqueData

from datetime import datetime

from ..guardFunctions.str_func import str_non_empty
from ..guardFunctions.int_func import int_is_int
from ..guardFunctions.date_func import date_is_date


class Transaction(UniqueData):

    _product_id: str = None
    _date: datetime = None
    _quantity: int = None
    _transaction_type: str = None
    
    def __init__(self, id: str, product_id: str, date: str | datetime, quantity: int, transaction_type: str, clss: str = None) -> None:
        super().__init__(id)
        
        self.product_id = product_id
        self.date = date
        self.quantity = quantity
        self.transaction_type = transaction_type
            
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
        _value = int_is_int(value)
        if _value is not None:
            self._quantity = _value

    @property
    def transaction_type(self) -> str:
        return self._transaction_type
    @transaction_type.setter
    def transaction_type(self, value) -> None:
        _value = str_non_empty(value)
        if _value is not None:
            self._transaction_type = _value

    @property
    def timestamp(self) -> str:
        if self._date is None:
            return None
        return self._date.strftime(self.date_format)

    def to_string(self) -> str:
        _list = self.to_list()
        _list[3] = "Qty: %i" % (_list[3])
        return " | ".join(_list)
    
    def to_list(self) -> list[any]:
        return [
            self.id,
            self.product_id,
            self.timestamp,
            self.quantity,
            self.transaction_type,
            type(self).__name__,
            ]
    
    @staticmethod
    def get_headers() -> list[str]:
        return [
            "id",
            "product_id",
            "date",
            "quantity",
            "transaction_type",
            "class",
        ]
    
    @staticmethod
    def get_types() -> list[type]:
        return [str, str, str, int, str, str]