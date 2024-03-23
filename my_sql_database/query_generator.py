from dataClasses import UniqueData
from dataClasses.dataTypes import Category, Product, Transaction

class QueryGenerator():

    def generate_table_for_class(self, class_type: UniqueData | type) -> str:
        _table_name = self._get_table_name(class_type)
        _column_definitions = self._get_column_definitions(class_type)
        return "CREATE TABLE IF NOT EXISTS %s (%s)" % (_table_name, _column_definitions)
    
    
    def generate_insertion_query(self, class_type: UniqueData | type) -> str:
        _table_name = self._get_table_name(class_type)
        _column_names = self._get_column_names(class_type)
        _column_symbols = self._get_column_symbols(class_type)
        return "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names, _column_symbols)

    def generate_search_query(self, class_type: UniqueData | type, *, search_term: str = "", output_rows: str = "*") -> str:
        _table_name = self._get_table_name(class_type)
        _query = "SELECT %s FROM %s %s" % (output_rows, _table_name, search_term)
        return _query.strip()


    '''
    def generete_search_query_beginning(self, class_type: UniqueData | type) -> str:
        _column_names = self._get_column_names(class_type)
        _table_name = self._get_table_name(class_type)
        return "SELECT %s FROM %s" % (_column_names, _table_name)
    '''



    def _get_sql_data_type_list(self, class_type: UniqueData | type) -> str:
        _type_list = class_type.get_types()
        return map(self._get_sql_data_type, _type_list)

    def _get_sql_data_type(self, var_type: type) -> str:
        if var_type is int:
            return "INT"
        else:
            return "VARCHAR(255)"
        
    def _get_table_name(self, class_type: type | UniqueData) -> str:
        if not isinstance(class_type, type):
            class_type = type(class_type)
        return class_type.__name__.lower()
        
    def _get_column_names(self, class_type: UniqueData):
        _headers = class_type.get_headers()
        return ', '.join(_headers)
        
    def _get_column_symbols(self, class_type: UniqueData):
        _headers = class_type.get_headers()
        _column_symbols = ['%s'] * len(_headers)
        return ', '.join(_column_symbols)





    def _get_column_definitions(self, class_type: UniqueData) -> str:
        _sql_definition_list = self._get_sql_definition_list(class_type)
        return ', '.join(_sql_definition_list)
        
    def _get_sql_definition_list(self, class_type: UniqueData) -> str:
        _headers = class_type.get_headers()
        _types = self._get_sql_data_type_list(class_type)
        return ["%s %s" % (a, b) for a, b in zip(_headers, _types)]
        
    
    def _get_class_arguments(self, unique_data: UniqueData):

        pass