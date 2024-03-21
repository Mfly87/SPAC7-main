from ..dataTypes import Category, Product, Transaction
from ..absDataTypes import UniqueData

class DataClassFactory():
    
    @staticmethod
    def _enlist_object(_obj: UniqueData) -> list[UniqueData]:
        return [_obj] if _obj.is_valid() else []

    @staticmethod
    def create_product(id : str, name : str, description : str, category_id : str, price : str, quantity : str, *args, **kwargs) -> list[Product]:
        return DataClassFactory._enlist_object( Product(id, name, description, category_id, price, quantity) )
    
    @staticmethod
    def create_category(id : str, name : str, description : str, *args, **kwargs) -> list[Category]:
        return DataClassFactory._enlist_object( Category(id, name, description) )
    
    @staticmethod
    def create_transaction(id : str, product_id : str, date : str, quantity : str, type, *args, **kwargs) -> list[Transaction]:
        return DataClassFactory._enlist_object( Transaction(id, product_id, date, quantity, type) )
        
    