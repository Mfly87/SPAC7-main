from .dataTypes import Category
from .dataTypes import Product
from .dataTypes import Transaction

class DataClassFactory():

    def create_product(self, id : str, name : str, description : str, category : Category, price : float, quantity : int) -> Product:
        return Product(id, name, description, category, price, quantity)
    
    def create_category(self, id : str, name : str, description : str) -> Category:
        return Category(id, name, description)
    
    def create_transaction(self, id, product, date, quantity, type) -> Transaction:
        return Transaction(id, product, date, quantity, type)
    
