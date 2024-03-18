from dataFaker import FakeCategory
from dataFaker import FakeProduct
from dataFaker import FakeTransaction

from dataClasses.dataTypes import Product


_category_list = FakeCategory().generate_fake_item_list()

_product_factory = FakeProduct()
_product = _product_factory.generate_fake_item_from_category_list(_category_list)

_transaction_factory = FakeTransaction()
for _ in range(10):
    _transaction = _transaction_factory.generate_fake_item(_product)
    print(_transaction.to_string())


for _ in range(10):
    _product = _product_factory.generate_fake_item_from_category_list(_category_list)
    print(_product.to_string())
