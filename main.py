from dataClasses.dataTypes import Product
from userInterface.user_interaction import UserInteraction
from warehouse import WarehouseOOP


from dataClasses.factory import FactoryCategory


from dataFaker import FakeCategory
from dataFaker import FakeProduct
from dataFaker import FakeTransaction

_wh = WarehouseOOP()

_product_factory = FakeProduct()
_category_factory = FakeCategory()
_transaction_factory = FakeTransaction()
_product_factory.set_seed(0)

_category_list = _category_factory.generate_fake_item_list()
for _category in _category_list:
    _wh.update_item(_category)

_product_list = []
for _ in range(100):
    _product = _product_factory.generate_fake_item_from_category_list(_category_list)
    _product_list.append(_product)
    _wh.update_item(_product)

for _ in range(100):
    _transaction = _transaction_factory.generate_fake_item_from_product_list(_product_list)
    _wh.update_item(_transaction)

print(str(_wh.item_count) + " items in warehouse")
#user_interaction = UserInteraction()
#user_interaction.start_interation()

#_data_list = _wh.get_items(["Prod-000050"])
_data_list = _wh.search_item("Coffee maker")
for _data in _data_list:
    if not isinstance(_data, Product):
        continue
    _price = _data.price
    while _price < 5000:
        _price *= 2
        _data._quantity += 100
    _wh.update_item(_data)

_data_list = _wh.search_item("010")
for _data in _data_list:
    print(_data.to_dict())


