from dataClasses import UniqueData
from dataClasses.dataTypes import Category, Product, Transaction

class QueryGenerator():

    def generate_table_for_class(self, unique_data: UniqueData) -> None:
        _table_name = self._get_table_name(unique_data)
        _column_definitions = self._get_column_definitions(unique_data)
        return "CREATE TABLE IF NOT EXISTS %s (%s)" % (_table_name, _column_definitions)
    
    def generate_insertion_query(self, unique_data: UniqueData) -> str:
        _table_name = self._get_table_name(unique_data)
        _headers = unique_data.get_headers()
        _column_names_combined = ', '.join(_headers)
        _column_symbols = ['%s'] * len(_headers)
        _column_symbols_combined = ', '.join(_column_symbols)
        return "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names_combined, _column_symbols_combined)




    def _get_sql_data_type(self, value: any) -> str:
        if isinstance(value, int):
            return "INT"
        else:
            return "VARCHAR(255)"
        
    def _get_table_name(self, class_type: type | UniqueData) -> str:
        if not isinstance(class_type, type):
            class_type = type(class_type)
        
        return class_type.__name__.lower()
    
    def _get_column_definitions(self, unique_data: UniqueData) -> str:
        _list = unique_data.to_list()
        _types = map(self._get_sql_data_type, _list)
        _headers = unique_data.get_headers()
        _combined = ["%s %s" % (a, b) for a, b in zip(_headers, _types)]
        return ', '.join(_combined)
    
    def _get_class_arguments(self, unique_data: UniqueData):

        pass