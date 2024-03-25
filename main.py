from my_sql_database import ServerConnection, SQLHandler, MySQLServerCredentials
from dataFaker import FakeWarehouseFiller
from warehouse import WarhouseMySQL
from faker import Faker

from userInterface import UserInteraction

print("\n\n")




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

_interaction = UserInteraction(warehouse)
_interaction.start_interation()

mysql_server.close_connection()
