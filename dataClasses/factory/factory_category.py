from .abs_factory import AbsFactory
from ..dataTypes import Category

class FactoryCategory(AbsFactory):

    def create_from_dict(self, obj_dict : dict[str,str]) -> list[Category]:
        self.create_from_params(
            obj_dict.get("id"),
            obj_dict.get("name"),
            obj_dict.get("description")
        )

    def create_from_params(self, id : str, name : str, description : str) -> list[Category]:
        _unique_data = Category(id, name, description)
        return self._ud_to_valid_list(_unique_data)