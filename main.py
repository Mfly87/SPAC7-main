from warehouse import WarehouseOOP
from dataFaker import FakeWarehouseFiller

from dataClasses.dataTypes import Category, Product, Transaction
_wh = WarehouseOOP()

FakeWarehouseFiller.fill_warehouse(_wh,100,100,100)

print(str(_wh.item_count) + " items in warehouse")
print(str(_wh.object_count) + " objects in warehouse")

_search_list = _wh.search_item("09")
print(str(len(_search_list)) + " results")
for _item in _search_list:
    print(_item.to_string())
    
_category_list = [i for i in _search_list if isinstance(i, Category)]
_product_list = [i for i in _search_list if isinstance(i, Product)]
_transaction_list = [i for i in _search_list if isinstance(i, Transaction)]

print(len(_category_list))
print(len(_product_list))
print(len(_transaction_list))