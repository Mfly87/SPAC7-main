from dataClasses import UniqueData
from dataClasses.dataTypes import Category
from .query_generator import QueryGenerator

from mysql.connector import MySQLConnection, Error
class SQLHandler:

    _current_database: str = ""

    def __init__(self, database_connector: MySQLConnection) -> None:
        self._database_connector: MySQLConnection = database_connector

    @property
    def database_connector(self) -> MySQLConnection:
        return self._database_connector
    
    @property
    def current_database(self):
        return self._current_database

    def connect_to_database(self, database_name: str):
        _creation_query = "CREATE DATABASE IF NOT EXISTS %s" % (database_name)
        self._execute_querty(_creation_query)

        _connection_query = "USE %s" % (database_name)
        self._execute_querty(_connection_query)

        self._current_database = database_name

    # This function should likely stored somewhere else, simply because of the danger
    def drop_table(self, class_type: UniqueData | type) -> None:
        _query = QueryGenerator.drop_table_for_class(class_type)
        self._execute_querty(_query)


    def create_table(self, unique_data_list: list[UniqueData]) -> None:
        if not unique_data_list:
            return
        
        class_type = type(unique_data_list[0])

        _create_table_query = QueryGenerator.generate_table_for_class(class_type)
        self._execute_querty(_create_table_query)

        _fill_table_query = QueryGenerator.generate_insert_many_query(class_type)
        self._execute_many_querty(_fill_table_query, unique_data_list)


    def search(self, class_type: UniqueData | type,*, search_term: str = ""):
        _query = QueryGenerator().generate_search_query(class_type, search_term = search_term)
        return self._execute_fetch_querty(_query)
        
    def update(self, unique_data: UniqueData):
        _query = QueryGenerator.generate_update_query(unique_data)
        self._execute_querty(_query)





    def _execute_many_querty(self, _query: str, _unique_data_list: list[UniqueData]) -> bool:
        try:
            with self.database_connector.cursor() as cursor:
                library_data = []
                for _unique_data in _unique_data_list:
                    library_data.append(tuple(_unique_data.to_list()))
                cursor.executemany(_query, library_data)
                return True
        except Error as e:
            print(f"An error occured during an executemany query {e}")
            return False
        
    def _execute_querty(self, _query: str) -> bool:
        try:
            with self.database_connector.cursor() as cursor:
                cursor.execute(_query)
                self.database_connector.commit()
                return True
        except Error as e:
            print(f"An error occured during an execute query {e}")
            return False
        
    def _execute_fetch_querty(self, _query: str) -> bool:
        try:
            with self.database_connector.cursor(dictionary=True) as cursor:
                cursor.execute(_query)
                return cursor.fetchall()
        except Error as e:
            print(f"An error occured during a fetch query {e}")
            return []
