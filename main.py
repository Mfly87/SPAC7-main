from my_sql_database import ConnectToDatabase, CreateLibraryTables

from dataClasses import UniqueData, DataClassFactory

from dataClasses.dataTypes import Category, Product, Transaction

from dataFaker import FakeCategory, FakeProduct, FakeTransaction

from dataFaker import FakeWarehouseFiller

from typing import Callable
from my_sql_database import QueryGenerator

print("\n\n\n")

mysql_server: ConnectToDatabase = ConnectToDatabase()
database_connection = mysql_server.connect_to_database("spac_7")
sql_database_table_creator = CreateLibraryTables()

'''
_dict = FakeWarehouseFiller.create_inventory_dict(10,20,10)
_type_list = [Category, Product, Transaction]

for _type in _type_list:
    _list = _dict[_type.__name__]
    sql_database_table_creator.create_table(database_connection, _list)
'''



_result: list[dict] = sql_database_table_creator.search(database_connection, Product, search_term = "WHERE name LIKE '%' AND id LIKE '%1_'")

_list: list[UniqueData] = []
for _dict in _result:
    for _obj in DataClassFactory.create_from_dict(**_dict):
        _list.append(_obj)

for _item in _list:
    print(_item.to_string())

_obj: Product = _list[2]
_obj.quantity = 9877

print(_obj.quantity)

sql_database_table_creator.update(database_connection, _obj)

_result: list[dict] = sql_database_table_creator.search(database_connection, Product, search_term = "WHERE id='%s'" % (_obj.id))

print("")
_list: list[UniqueData] = []
for _dict in _result:
    for _obj in DataClassFactory.create_from_dict(**_dict):
        print(_obj.to_string())