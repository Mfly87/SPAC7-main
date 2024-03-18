from .category import Category
from .product import Product

class DataClassFactory():

    def create_product(self, id : str, name : str, description : str, category : Category, price : float, quantity : int):
        return Product(id, name, description, category, price, quantity)
    
    def create_category(self, id : str, name : str, description : str):
        return Category(id, name, description)