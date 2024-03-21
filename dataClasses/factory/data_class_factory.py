from ..dataTypes import Category, Product, Transaction
from ..absDataTypes import UniqueData

class DataClassFactory():

    @staticmethod
    def create_product(id : str, name : str, description : str, category_id : str, price : str, quantity : str, *args, **kwargs) -> list[Product]:
        _obj = Product(id, name, description, category_id, price, quantity)
        return DataClassFactory._create_valid_list_form(_obj)
    
    @staticmethod
    def create_category(id : str, name : str, description : str, *args, **kwargs) -> list[Category]:
        _obj = Category(id, name, description)
        return DataClassFactory._create_valid_list_form(_obj)
    
    @staticmethod
    def create_transaction(id : str, product_id : str, date : str, quantity : str, type, *args, **kwargs) -> list[Transaction]:
        _obj = Transaction(id, product_id, date, quantity, type)
        return DataClassFactory._create_valid_list_form(_obj)
    
    @staticmethod
    def _create_valid_list_form(ud: UniqueData) -> list[UniqueData]:
        _dict = ud.__dict__
        for _value in _dict.values():
            if _value is None:
                return []
        return [ud]
    