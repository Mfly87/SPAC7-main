from ..absDataTypes import UniqueData

from datetime import datetime
from .product import Product

class Transaction(UniqueData):
    _date : datetime = datetime(1900,1,1)
    
    def __init__(self, id: str, product_id: str, date: datetime, quantity: int, type: str) -> None:
        super().__init__(id)
        
        self._product_id : str = product_id
        self.change_date(date)
        self.change_quantity(quantity)

        self._quantity : str = quantity
        self._type : str = type
    
    @property
    def product_id(self) -> Product:
        return self._product_id
    
    @property
    def date(self) -> datetime:
        return self._date
    
    @property
    def timestamp(self) -> str:
        return self.date.strftime(self.date_format)
    
    def change_date(self, date : str | datetime) -> None:
        _date = self._convert_to_datetime_or_none(date)
        if _date is not None:
            self._date = _date

    def change_quantity(self, quantity : str | int) -> None:
        _quantity = self._convert_to_int_or_none(quantity)
        if _quantity is not None:
            self._quantity = _quantity

    @property
    def quantity(self) -> int:
        return self._quantity
    
    @property
    def type(self) -> str:
        return self._type
        
    def to_dict(self) -> dict[str,str]:
        return {
            "class": type(self).__name__,
            "id": self.id,
            "product_id": self.product_id,
            "date": self.timestamp,
            "type": self.type,
            "quantity": str(self.quantity),
        }

    def to_string(self) -> str:
        return " | ".join([
            self.id,
            self.product_id,
            self.timestamp,
            "Qty: " + str(self.quantity),
            self.type,
        ])
    
    def _convert_to_datetime_or_none(self, value : any) -> int | None:
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, self.date_format)
            except ValueError as ex:
                template = "   An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print( message )
                return
        if isinstance(value, datetime):
            return value
        return None