from my_sql_database import ConnectToDatabase, CreateLibraryTables

from dataClasses import UniqueData

from dataClasses.dataTypes import Category, Product, Transaction

from dataFaker import FakeCategory, FakeProduct, FakeTransaction

from typing import Callable


mysql_server: ConnectToDatabase = ConnectToDatabase()
database_connection = mysql_server.connect_to_database("spac_7")
sql_database_table_creator = CreateLibraryTables()






_fatory_category = FakeCategory()
_category_list: list[Category] = []
for _ in range(20):
    for _category in _fatory_category.generate_fake_item():
        _category_list.append(_category)

sql_database_table_creator.create_table(database_connection, _category_list)
