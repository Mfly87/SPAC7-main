from .abs_faker import AbsFaker

from dataClasses.factory import DataClassFactory
from dataClasses.dataTypes import Category
from dataClasses.dataTypes import Product

class FakeProduct(AbsFaker):
    @property
    def id_tag(self):
        return "Prod"
    
    def generate_fake_item_from_category_list(self, category_list : list[Category]) -> list[Product]:
        _category : Category = self._get_rand_item(category_list)
        return self.generate_fake_item(_category)

    def generate_fake_item(self, catagory : Category) -> list[Product]:
        _price = self._create_int(6,60)*50 - 1
        _quantity = self._create_int(0,50)

        factory = DataClassFactory()
        return factory.create_product(
            self.get_next_id(),
            self._generate_product_name(catagory.name),
            self._create_sentence(),
            catagory.id,
            str(_price),
            str(_quantity)
        )

    def _generate_product_name(self, catagory : str):
        return " ".join([
            self._create_last_name(),
            catagory,
            self._create_awesomizer()
        ])
