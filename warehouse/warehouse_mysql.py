from .abs_warehouse import AbsWarehouse
from dataClasses.factory import DataClassFactory
from my_sql_database import SQLHandler
from dataClasses.absDataTypes import UniqueData

from typing import TypeVar
T = TypeVar("T")

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

    def search_all_tables_of_subclass(self, subclass: UniqueData | type, _query_specifier: str) -> list[UniqueData]:
        _class_list = []
        for _type in self.mysql_handler.get_table_types():
            if issubclass(_type, subclass):
                _class_list.append(_type)
        return self.search_multiple_tables(_class_list, _query_specifier)

    def search_multiple_tables(self, _class_list: list[UniqueData | type], _query_specifier: str) -> list[UniqueData]:
        _unique_data_list: list[UniqueData] = []
        for _type in _class_list:
            _unique_data_list += self.search_table(_type, _query_specifier)
        return _unique_data_list
    
    def search_table(self, _type: UniqueData | type, _query_specifier: str) -> list[UniqueData]:
        _result = self.mysql_handler.search(_type, search_term = _query_specifier)
        return self._unpack_unique_data_dict_to_object(_result)

    def get_items(self):
        pass

    def search_item(self, search_string: str) -> list[UniqueData]:
        pass
    
    def update_item(self, unique_data: UniqueData, change_dict):
        _dict = unique_data.to_dict()
        _dict.update(change_dict)

        _unique_data_list = self._unpack_unique_data_dict_to_object([_dict])
        for _unique_data in _unique_data_list:
            self.mysql_handler.update_item(_unique_data)
        
        return _unique_data_list
    



    def _unpack_unique_data_dict_to_object(self, search_result: list[dict]) -> list[UniqueData]:
        _unique_data_list: list[UniqueData] = []
        for _dict in search_result:
            for _unique_data in DataClassFactory.create_from_dict(**_dict):
                _unique_data_list.append(_unique_data)
        return _unique_data_list
        

    def delete_item(self):
        pass