from ..dataTypes import Category, Product, Transaction
from ..absDataTypes import UniqueData

class DataClassFactory():

    def create_product(self, id : str, name : str, description : str, category_id : str, price : str, quantity : str, *args, **kwargs) -> list[Product]:
        _obj = Product(id, name, description, category_id, price, quantity)
        return self._create_valid_list_form(_obj)
    
    def create_category(self, id : str, name : str, description : str, *args, **kwargs) -> list[Category]:
        _obj = Category(id, name, description)
        return self._create_valid_list_form(_obj)
    
    def create_transaction(self, id : str, product_id : str, date : str, quantity : str, type, *args, **kwargs) -> list[Transaction]:
        _obj = Transaction(id, product_id, date, quantity, type)
        return self._create_valid_list_form(_obj)
    
    def _create_valid_list_form(self, ud: UniqueData) -> list[UniqueData]:
        _dict = ud.__dict__
        for _value in _dict.values():
            if _value is None:
                return []
        return [ud]
    