from .category import Category

class Product():
    def __init__(self, id : str, name : str, description : str, category : Category, price : float, quantity : int):
        self._id : str = id
        self._name : str = name
        self._description : str = description
        self._category : Category = category
        self._price : float = price
        self._quantity : int = quantity

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def category(self) -> Category:
        return self._category
    
    @property
    def price(self) -> float:
        return self.price
    
    @property
    def quantity(self) -> int:
        return self._quantity

