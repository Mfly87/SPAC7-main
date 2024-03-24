from .abs_warehouse import AbsWarehouse
from dataClasses.factory import DataClassFactory
from my_sql_database import SQLHandler
from dataClasses.absDataTypes import UniqueData, UniqueNamedData

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
        _query_seach = f"WHERE name LIKE '%{search_string}%' OR description LIKE '%{search_string}%'"
        _unique_data_list = []
        for _type in self.mysql_handler.get_table_types():
            if not issubclass(_type, UniqueNamedData):
                continue
            _result = self.mysql_handler.search(_type, search_term = _query_seach)
            for _dict in _result:
                for _unique_data in DataClassFactory.create_from_dict(**_dict):
                    _unique_data_list.append(_unique_data)
        self._prev_search_list = _unique_data_list
        return self.prev_search_list

    def update_item(self, unique_data: UniqueData):
        _new_item = True
        for _prev_search in self.prev_search_list:
            if type(_prev_search) != type(unique_data):
                continue
            if _prev_search.id != unique_data.id:
                continue
            _new_item = False
            break

        if _new_item:
            print("Item doesn't match anything previously searched for.")

        self.mysql_handler.update_item(unique_data)

    def delete_item(self):
        pass