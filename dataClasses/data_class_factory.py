from .category import Category
from .product import Product

class DataClassFactory():

    def create_product(id : str, name : str, description : str, category : Category, price : float, quantity : int):
        return Product(id, name, description, category, price, quantity)
    
    def create_category(id : str, name : str, description : str):
        return Product(id, name, description)