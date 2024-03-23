from ..dataTypes import Category, Product, Transaction
from ..absDataTypes import UniqueData
from datetime import datetime

from typing import Callable

class DataClassFactory():
    
    @staticmethod
    def _enlist_object(_obj: UniqueData) -> list[UniqueData]:
        return [_obj] if _obj.is_valid() else []
    
    @staticmethod
    def create_from_dict(**kwargs) -> list[UniqueData]:
        func = DataClassFactory._get_creation_func(**kwargs)
        return func(**kwargs)

    @staticmethod
    def _get_creation_func(**kwargs) -> Callable[[dict[str, any]], list[UniqueData]]:
        match kwargs.get("class", ""):
            case Category.__name__:
                return DataClassFactory.create_category
            case Product.__name__:
                return DataClassFactory.create_product
            case Transaction.__name__:
                return DataClassFactory.create_transaction
            case _:
                return DataClassFactory.create_null

    @staticmethod
    def create_null(*args, **kwargs) -> list[UniqueData]:
        return []

    @staticmethod
    def create_product(id : str, name : str, description : str, category_id : str, price : int, quantity : int, *args, **kwargs) -> list[Product]:
        return DataClassFactory._enlist_object( Product(id, name, description, category_id, price, quantity) )
    
    @staticmethod
    def create_category(id : str, name : str, description : str, *args, **kwargs) -> list[Category]:
        return DataClassFactory._enlist_object( Category(id, name, description) )
    
    @staticmethod
    def create_transaction(id : str, product_id : str, date : str | datetime, quantity : int, transaction_type, *args, **kwargs) -> list[Transaction]:
        return DataClassFactory._enlist_object( Transaction(id, product_id, date, quantity, transaction_type) )
        
    