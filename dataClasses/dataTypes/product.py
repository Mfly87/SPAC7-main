from ..absDataTypes import UniqueNamedData
from .category import Category

class Product(UniqueNamedData):
    _price : int = 0
    _quantity : int = 0

    def __init__(self, id : str, name : str, description : str, category_id : str, price : int, quantity : int) -> None:
        super().__init__(id, name, description)

        self._category_id : str = category_id
        self.change_price(price)
        self.change_quantity(quantity)
    
    @property
    def category_id(self) -> str:
        return self._category_id
    
    @property
    def price(self) -> str:
        return self._price
    
    @property
    def quantity(self) -> str:
        return self._quantity

    def change_price(self, price : str | int) -> None:
        _price = self._convert_to_int_or_none(price)
        if isinstance(_price, str):
            self._price = _price
    
    def change_quantity(self, quantity : str | int) -> None:
        _quantity = self._convert_to_int_or_none(quantity)
        if isinstance(_quantity, str):
            self._quantity = _quantity

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