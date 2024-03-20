from .abs_factory import AbsFactory
from ..dataTypes import Category

class FactoryCategory(AbsFactory):

    def create(self, id : str, name : str, description : str , **kwargs) -> list[Category]:
        _unique_data = Category(id, name, description)
        return self._ud_to_valid_list(_unique_data)