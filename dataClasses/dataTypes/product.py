from ..absDataTypes import UniqueNamedData
from .category import Category

class Product(UniqueNamedData):
    def __init__(self, id : str, name : str, description : str, category_id : str, price : str, quantity : str) -> None:
        super().__init__(id, name, description)

        self._category_id : str = category_id
        self._price : str = price
        self._quantity : str = quantity
    
    @property
    def category_id(self) -> str:
        return self._category_id
    
    @property
    def price(self) -> str:
        return self._price
    
    @property
    def quantity(self) -> str:
        return self._quantity
    
    def to_dict(self) -> dict[str,str]:
        return {
            "class": type(self).__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category_id": self.category_id,
            "price": self.price,
            "quantity": self.quantity,
        }
    
    def to_string(self) -> str:
        return " | ".join([
            self.id,
            self.name,
            self.description,
            self.category_id,
            self.price + ",-kr.",
            "Qty: " + self.quantity
        ])