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

_product_faker.set_seed(0)
for _product in _product_faker.generate_fake_item_from_category_list(_category_list):
    _product_list.append(_product)

_product_faker.set_seed(0)
for _product in _product_faker.generate_fake_item_from_category_list(_category_list):
    _product_list.append(_product)

print(_product_list[0].to_string())
print(_product_list[1])
print("_product_list[1]")


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
#user_interaction = UserInteraction()
#user_interaction.start_interation()


_p0 = _wh.get_items(["Prod-000005"])[0]
_d0 = _p0.to_dict()
print(_d0)

_d0 |= {"price": "42"}

_factory = DataClassFactory()
_p1 = _factory.create_product(**_d0)[0]

print(_p0.to_dict())
print(_p0.to_string())
print(_p1.to_string())

_wh.update_item(_p1)

_p2: Product = _wh.get_items(["Prod-000005"])[0]
print(_p2.to_string())

_p2.change_price(None)

_t = _transaction_list[0]
print(_t.to_string())

_t.change_date("1042-12-1")
print(_t.to_string())

_wh.update_item(_t)

_t2: Product = _wh.get_items([_t.id])[0]
print(_t2.to_string())