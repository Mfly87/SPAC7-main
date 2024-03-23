from dataClasses import UniqueData
from dataClasses.dataTypes import Category, Product, Transaction

class QueryGenerator():

    def generate_table_for_class(self, class_type: UniqueData | type) -> str:
        _table_name = self._get_table_name(class_type)
        _column_definitions = self._get_column_definitions(class_type)
        return "CREATE TABLE IF NOT EXISTS %s (%s)" % (_table_name, _column_definitions)
    
    def drop_table_for_class(self, class_type: UniqueData | type) -> str:
        _table_name = self._get_table_name(class_type)
        return "DROP TABLE %s" % (_table_name)
        
    def generate_insertion_query(self, class_type: UniqueData | type) -> str:
        _table_name = self._get_table_name(class_type)
        _column_names = self._get_column_names(class_type)
        _column_symbols = self._get_column_symbols(class_type)
        return "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names, _column_symbols)

    def generate_search_query(self, class_type: UniqueData | type, *, search_term: str = "", output_rows: str = "*") -> str:
        _table_name = self._get_table_name(class_type)
        _query = "SELECT %s FROM %s %s" % (output_rows, _table_name, search_term)
        return _query.strip()
    
    def generate_update_query(self,unique_data: UniqueData) -> str:
        _table_name = self._get_table_name(unique_data)
        _unique_data_values = self._unique_data_values(unique_data)
        return "UPDATE %s SET %s WHERE id='%s'" % (_table_name, _unique_data_values, unique_data.id)



    def _unique_data_values(self, unique_data: UniqueData):
        _headers = unique_data.get_headers()
        _sql_value_list = self._sql_value_list(unique_data)
        _zip = ["%s = %s" % (a, b) for a, b in zip(_headers, _sql_value_list)]
        return ", ".join(_zip)

    def _sql_value_list(self,unique_data: UniqueData) -> list[str]:
        _list = []
        for _item in unique_data.to_list():
            if isinstance(_item, str):
                _list.append("'%s'" % (_item))
            else:
                _list.append("%s" % (_item))
        return _list




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
        