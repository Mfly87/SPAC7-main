from .abs_warehouse import AbsWarehouse
from dataClasses.factory import DataClassFactory
from my_sql_database import SQLHandler
from dataClasses.absDataTypes import UniqueData, UniqueNamedData

from dataClasses.dataTypes import Category

from my_sql_database import QueryGenerator

class WarhouseMySQL(AbsWarehouse):

    _prev_search_list: list[UniqueData] = []

    def __init__(self, mysql_handler: SQLHandler, database_name: str) -> None:
        self._mysql_handler: SQLHandler = mysql_handler
        self._database_name: str = database_name

        # Technically this could be done before each function for safety, but I'm not sure if that's normal
        self.mysql_handler.connect_to_database(self.database_name)


    @property
    def mysql_handler(self) -> SQLHandler:
        return self._mysql_handler
    
    @property
    def database_name(self) -> str:
        return self._database_name 
    
    @property
    def prev_search_list(self) -> list[UniqueData]:
        return self._prev_search_list 

    def clear_warehouse(self):
        for _class in self.mysql_handler.get_table_names():
            self.mysql_handler.drop_table(_class)

    def set_inventory(self, inventory_dict: dict[str, list[UniqueData]]):
        self.clear_warehouse()

        for _unique_data_list in inventory_dict.values():
            self.mysql_handler.create_table(_unique_data_list)


    def get_items(self):
        pass

    def search_item(self, search_string: str) -> list[UniqueData]:
        pass
    
    def update_item(self, unique_data: UniqueData):
        self.mysql_handler.update_item(unique_data)

    def delete_item(self):
        pass