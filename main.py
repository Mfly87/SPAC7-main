from dataClasses.dataTypes import Product
from dataClasses.dataTypes import Transaction

from userInterface.user_interaction import UserInteraction
from warehouse import WarehouseOOP


from dataClasses.factory import DataClassFactory


from dataFaker import FakeCategory
from dataFaker import FakeProduct
from dataFaker import FakeTransaction

_wh = WarehouseOOP()

_product_faker = FakeProduct()
_category_faker = FakeCategory()
_transaction_faker = FakeTransaction()
_product_faker.set_seed(0)

_category_list = _category_faker.generate_fake_item_list()
for _category in _category_list:
    _wh.update_item(_category)

_product_list : list[Product] = []

for _ in range(100):
    for _product in _product_faker.generate_fake_item_from_category_list(_category_list):
        _product_list.append(_product)
        _wh.update_item(_product)

_transaction_list : list[Transaction] = []
for _ in range(100):
    for _transaction in _transaction_faker.generate_fake_item_from_product_list(_product_list):
        _transaction_list.append(_transaction)
        _wh.update_item(_transaction)

print(str(_wh.item_count) + " items in warehouse")

print("categories: " + str(len(_category_list)))
print("products: " + str(len(_product_list)))
print("transactions: " + str(len(_transaction_list)))

_search_list = _wh.search_item("09")
print(str(len(_search_list)) + " results")
for _item in _search_list:
    print(_item.to_string())