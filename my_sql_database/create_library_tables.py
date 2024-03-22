from typing import Tuple
from dataClasses import UniqueData

from mysql.connector import MySQLConnection, Error
class CreateLibraryTables:
    def create_table(self, database_connector: MySQLConnection, unique_data_list: list[UniqueData]) -> None:
        
        if not unique_data_list:
            return
        
        create_table_query = self._generete_new_table_query(unique_data_list[0])
        insert_query = self._generate_insertion_query(unique_data_list[0])

        try:
            # Connect to the database
            with database_connector.cursor() as cursor:
                cursor.execute(create_table_query)

                library_data = []
                for _unique_data in unique_data_list:
                    library_data.append(tuple(_unique_data.to_list()))

                cursor.executemany(insert_query, library_data)

            # Commit changes
            database_connector.commit()

        except Error as e:
            print("Error creating table: %s" % (e))
            raise
        

    def _generate_insertion_query(self, unique_data: UniqueData) -> str:
        _table_name = self._get_table_name(unique_data)

        _headers = unique_data.get_headers()
        _column_names_combined = ', '.join(_headers)
        _column_symbols = ['%s'] * len(_headers)
        _column_symbols_combined = ', '.join(_column_symbols)
        return "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names_combined, _column_symbols_combined)


    def _generete_new_table_query(self,unique_data: UniqueData) -> str:
        _table_name = self._get_table_name(unique_data)

        _column_definitions = self._create_column_definitions(unique_data)
        return "CREATE TABLE IF NOT EXISTS %s (%s)" % (_table_name, _column_definitions)

    def _create_column_definitions(self, unique_data: UniqueData) -> str:
        _list = unique_data.to_list()
        _types = map(self._get_sql_data_type, _list)

        _headers = unique_data.get_headers()
        
        _combined = ["%s %s" % (a, b) for a, b in zip(_headers, _types)]

        return ', '.join(_combined)

    def _get_sql_data_type(self, value: any) -> str:
        if isinstance(value, int):
            return "INT"
        else:
            return "VARCHAR(255)"
        
    def _get_table_name(self, unique_data: UniqueData) -> str:
        return unique_data.to_dict()["class"].lower()