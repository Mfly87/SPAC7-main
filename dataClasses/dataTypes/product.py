from ..absDataTypes import UniqueNamedData

from ..guardFunctions.int_func import int_zero_or_greater
from ..guardFunctions.str_func import str_non_empty

class Product(UniqueNamedData):

    _category_id: str = None
    _price: int = None
    _quantity: int = None

    def __init__(self, id : str, name : str, description : str, category_id : str, price : int, quantity : int) -> None:
        super().__init__(id, name, description)

        self.category_id = category_id
        self.price = price
        self.quantity = quantity
    
    @property
    def category_id(self) -> str:
        return self._category_id
    @category_id.setter
    def category_id(self, value) -> None:
        _value = str_non_empty(value)
        if _value is not None:
            self._category_id = _value
    
    @property
    def price(self) -> int:
        return self._price
    @price.setter
    def price(self, value) -> None:
        _value = int_zero_or_greater(value)
        if _value is not None:
            self._price = _value
    
    @property
    def quantity(self) -> str:
        return self._quantity
    @quantity.setter
    def quantity(self, value) -> None:
        _value = int_zero_or_greater(value)
        if _value is not None:
            self._quantity = _value

    def to_dict(self) -> dict[str,any]:
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
            str(self.price) + ",-kr.",
            "Qty: " + str(self.quantity)
        ])  