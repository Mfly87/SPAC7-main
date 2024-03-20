from .abs_factory import AbsFactory
from ..dataTypes import Product
from ..dataTypes import Category

class FactoryCategory(AbsFactory):

    def create(self, id : str, name : str, description : str, category_id : str, price : float, quantity : int, **kwargs) -> Product:
        _unique_data = Product(id, name, description, category_id, price, quantity)
        return self._ud_to_valid_list(_unique_data)