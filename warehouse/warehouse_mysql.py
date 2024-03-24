from .abs_warehouse import AbsWarehouse
from my_sql_database import SQLHandler
from dataClasses import UniqueData

class WarhouseMySQL(AbsWarehouse):
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

    def clear_warehouse(self):
        for _class in self.mysql_handler.get_table_names():
            self.mysql_handler.drop_table(_class)

    def set_inventory(self, inventory_dict: dict[str, list[UniqueData]]):
        self.clear_warehouse()

        for _unique_data_list in inventory_dict.values():
            self.mysql_handler.create_table(_unique_data_list)


    def search_item(self):
        pass

    def get_items(self):
        pass

    def update_item(self):
        pass

    def delete_item(self):
        pass