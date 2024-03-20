from ..absDataTypes import UniqueNamedData
from .category import Category

class Product(UniqueNamedData):
    def __init__(self, id : str, name : str, description : str, category_id : str, price : float, quantity : int) -> None:
        super().__init__(id, name, description)

        self._category_id : Category = category_id
        self._price : float = price
        self._quantity : int = quantity
    
    @property
    def category_id(self) -> Category:
        return self._category_id
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    def to_dict(self) -> dict[str,str]:
        return {
            "class": type(self).__name__,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category_id": self.category_id,
            "price": str(self.price),
            "quantity": str(self.quantity),
        }
    
    def to_string(self) -> str:
        return " | ".join([
            self.id,
            self.name,
            self.description,
            self.category_id,
            str(self.price) + ",-kr.",
            "Qty: " + str(self.quantity)
        ])