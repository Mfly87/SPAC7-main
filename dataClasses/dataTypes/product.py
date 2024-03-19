from ..absDataTypes import UniqueNamedData
from .category import Category

class Product(UniqueNamedData):
    def __init__(self, id : str, name : str, description : str, category : Category, price : float, quantity : int) -> None:
        super().__init__(id, name, description)

        self._category : Category = category
        self._price : float = price
        self._quantity : int = quantity
    
    @property
    def category(self) -> Category:
        return self._category
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    def to_string(self):
        return " | ".join([
            self.id,
            self.name,
            self.description,
            self.category.name,
            str(self.price) + ",-kr.",
            "Qty: " + str(self.quantity)
        ])