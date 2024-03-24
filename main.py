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

#FakeWarehouseFiller.fill_warehouse(warehouse, _categories, _products, _transactions)

_list = warehouse.search_item("05")
for _item in _list:
    print(_item.to_string())

_obj: Product = _list[-1]
_obj.quantity = 999 if _obj.quantity == 0 else 0

warehouse.update_item(_obj)

for _item in warehouse.search_item(_obj.name):
    print(_item.to_string())