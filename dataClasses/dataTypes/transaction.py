from ..absDataTypes import UniqueData

from datetime import datetime
from .product import Product

class Transaction(UniqueData):
    def __init__(self, id : str, product_id : str, date : datetime, quantity : int, type : str) -> None:
        super().__init__(id)
        
        self._product_id : str = product_id
        self._date : datetime = date
        self._quantity : int = quantity
        self._type : str = type
    
    @property
    def product_id(self) -> Product:
        return self._product_id
    
    @property
    def date(self) -> datetime:
        return self._date
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    @property
    def type(self) -> str:
        return self._type
    
    @property
    def timestamp(self):
        return str(self.date)

    def to_dict(self) -> dict[str,str]:
        return {
            "class": type(self).__name__,
            "id": self.id,
            "product_id": self.product_id,
            "timestamp": self.timestamp,
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