from ..absDataTypes import UniqueData

from datetime import datetime
from .product import Product

class Transaction(UniqueData):
    def __init__(self, id : str, product : Product, date : datetime, quantity : int, type : str) -> None:
        super().__init__(id)
        
        self._product : Product = product
        self._date : datetime = date
        self._quantity : int = quantity
        self._type : str = type
    
    @property
    def product(self) -> Product:
        return self._product
    
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

    def to_string(self):
        return " | ".join([
            self.id,
            self.product.id,
            self.timestamp,
            "Qty: " + str(self.quantity),
            self.type,
        ])