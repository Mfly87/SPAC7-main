from my_sql_database import ServerConnection, SQLHandler, MySQLServerCredentials

from dataClasses import UniqueData, DataClassFactory

from dataClasses.dataTypes import Category, Product, Transaction

from dataFaker import FakeWarehouseFiller
from warehouse import WarhouseMySQL
from faker import Faker

print("\n\n\n")





_database_name = "spac_7"

_credentials = MySQLServerCredentials(
    "localhost",
    "root",
    "Kom12345",
    3306
)

_categories = 100
_products = 100
_transactions = 100

Faker.seed(0)




mysql_server: ServerConnection = ServerConnection()
mysql_server.connect_to_server(_credentials)

sql_handler = SQLHandler(mysql_server.mysql_connection)
warehouse = WarhouseMySQL(sql_handler, _database_name)

FakeWarehouseFiller.fill_warehouse(warehouse, _categories, _products, _transactions)


_result: list[dict] = sql_handler.search(Product, search_term = "WHERE description LIKE '%wh%'")

print("%i search results" % (len(_result)))

_unique_data_list: list[UniqueData] = []
for _dict in _result:
    for _obj in DataClassFactory.create_from_dict(**_dict):
        _unique_data_list.append(_obj)

for _item in _unique_data_list:
    print(_item.to_string())

_obj: Product = _unique_data_list[2]
_obj.quantity = 9877

sql_handler.update_item(_obj)

_result: list[dict] = sql_handler.search(type(_obj), search_term = "WHERE id='%s'" % (_obj.id))

print("")
_unique_data_list: list[UniqueData] = []
for _dict in _result:
    for _obj in DataClassFactory.create_from_dict(**_dict):
        print(_obj.to_string())
