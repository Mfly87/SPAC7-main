from my_sql_database import ConnectToDatabase, CreateLibraryTables

from dataClasses.dataTypes import Category, Product, Transaction

from dataFaker import FakeCategory

from typing import Callable


mysql_server: ConnectToDatabase = ConnectToDatabase()
database_connection = mysql_server.connect_to_database("spac_7")
sql_database_table_creator = CreateLibraryTables()

_category_header = ["id", "name", "description"]
_category_types = ["VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)"]



_product_header = ["id", "name", "description", "category_id", "price", "quantity"]
_product_types = ["VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "INT", "INT"]

_transaction_header = ["id", "product_id", "date", "quantity", "type"]
_transaction_types = ["VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "INT", "VARCHAR(255)"]

_fatory_category = FakeCategory()
_category_list: list[Category] = []
for _ in range(20):
    for _category in _fatory_category.generate_fake_item():
        _category_list.append(tuple(_category.to_string().split(" | ")))

print(_category.to_string())


func: Callable[[Category], list[str]] = lambda x : [x.id, x.name, x.description]



print(func(_category))

#sql_database_table_creator.create_table("category", _category_header, _category_types, _category_list, database_connection)

from warehouse import WarehouseOOP
from dataFaker import FakeWarehouseFiller

_category_count = 1
_product_count = 1
_transaction_count = 1

wh = WarehouseOOP()
FakeWarehouseFiller.fill_warehouse(wh, _category_count, _product_count, _transaction_count)

_search_list = wh.search_item("0")

_category_list = [i for i in _search_list if isinstance(i, Category)]
for _obj in _category_list:
    print(_obj.to_string())
    
_product_list = [i for i in _search_list if isinstance(i, Product)]
for _obj in _product_list:
    print(_obj.to_string())
    
_transaction_list = [i for i in _search_list if isinstance(i, Transaction)]
for _obj in _transaction_list:
    print(_obj.to_string())