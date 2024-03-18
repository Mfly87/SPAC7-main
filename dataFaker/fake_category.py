from .abs_faker import AbsFaker
from dataClasses import Category
from dataClasses import DataClassFactory

class FakeCategory(AbsFaker):
    @property
    def id_tag(self):
        return "Cat"

    @property
    def fake_category_names(self):
        return [
            "Refrigerator",
            "Oven",
            "Air fryer",
            "Microwave",
            "Dishwasher",
            "Washing machine",
            "Dryer",
            "Vacuum cleaner",
            "Air conditioner",
            "Heater",
            "Iron",
            "Blender",
            "Toaster",
            "Coffee maker",
            "Kettle",
            "Electric fan"
        ]
    
    def generate_fake_item_list(self) -> list[Category]:
        _category_list = []
        for _category_name in self.fake_category_names:
            _category = self.generate_fake_item(_category_name)
            _category_list.append(_category)
        return _category_list

    def generate_fake_item(self, category_name : str) -> Category:
        _factory = DataClassFactory()
        return _factory.create_category(
            self.get_next_id(),
            category_name,
            self._create_sentence()
        )