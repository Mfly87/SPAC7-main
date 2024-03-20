from ..absDataTypes import UniqueData

from datetime import datetime
from .product import Product

class Transaction(UniqueData):
    def __init__(self, id : str, product_id : str, date : str, quantity : str, type : str) -> None:
        super().__init__(id)
        
        self._product_id : str = product_id
        self._date : str = date
        self._quantity : str = quantity
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
    
    def to_dict(self) -> dict[str,str]:
        return {
            "class": type(self).__name__,
            "id": self.id,
            "product_id": self.product_id,
            "date": self.date,
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