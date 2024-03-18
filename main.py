from dataFaker import FakeCategory
from dataFaker import FakeProduct
from dataClasses.dataTypes import Product

_category_list = FakeCategory().generate_fake_item_list()
_product_factory = FakeProduct()
for _ in range(100):
    _product = _product_factory.generate_fake_item_from_category_list(_category_list)
    print(_product.to_string())