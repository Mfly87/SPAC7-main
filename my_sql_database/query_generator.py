from dataClasses import UniqueData

class QueryGenerator():

    @staticmethod
    def drop_table_for_class(class_type: UniqueData | type) -> str:
        _table_name = QueryGenerator._get_table_name(class_type)
        return "DROP TABLE IF EXISTS %s" % (_table_name)
    
    @staticmethod
    def generate_table_for_class(class_type: UniqueData | type) -> str:
        _table_name = QueryGenerator._get_table_name(class_type)
        _column_definitions = QueryGenerator._get_column_definitions(class_type)
        return "CREATE TABLE IF NOT EXISTS %s (%s)" % (_table_name, _column_definitions)
        
    @staticmethod
    def generate_insert_query(class_type: UniqueData | type) -> str:
        _table_name = QueryGenerator._get_table_name(class_type)
        _column_names = QueryGenerator._get_column_names(class_type)
        _column_values = QueryGenerator._get_column_values(class_type)
        return "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names, _column_values)
        
    @staticmethod
    def generate_insert_many_query(class_type: UniqueData | type) -> str:
        _table_name = QueryGenerator._get_table_name(class_type)
        _column_names = QueryGenerator._get_column_names(class_type)
        _column_symbols = QueryGenerator._get_column_symbols(class_type)
        return "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names, _column_symbols)

    @staticmethod
    def generate_search_query(class_type: UniqueData | type, *, search_term: str = "", output_rows: str = "*") -> str:
        _table_name = QueryGenerator._get_table_name(class_type)
        _query = "SELECT %s FROM %s %s" % (output_rows, _table_name, search_term)
        return _query.strip()
    
    @staticmethod
    def generate_update_query(unique_data: UniqueData) -> str:
        _table_name = QueryGenerator._get_table_name(unique_data)
        _unique_data_update_values = QueryGenerator._unique_data_update_values(unique_data)
        return "UPDATE %s SET %s WHERE id='%s'" % (_table_name, _unique_data_update_values, unique_data.id)



    @staticmethod
    def _get_column_values(unique_data: UniqueData):
        _list = unique_data.to_list()
        return ", ".join(_list)
    
    @staticmethod
    def _unique_data_update_values(unique_data: UniqueData):
        _headers = unique_data.get_headers()
        _sql_value_list = QueryGenerator._sql_value_list(unique_data)
        _zip = ["%s = %s" % (a, b) for a, b in zip(_headers, _sql_value_list)]
        return ", ".join(_zip)

    @staticmethod
    def _sql_value_list(unique_data: UniqueData) -> list[str]:
        _list = []
        for _item in unique_data.to_list():
            if isinstance(_item, str):
                _list.append("'%s'" % (_item))
            else:
                _list.append("%s" % (_item))
        return _list




    @staticmethod
    def _get_sql_data_type_list(class_type: UniqueData | type) -> str:
        _type_list = class_type.get_types()
        return map(QueryGenerator._get_sql_data_type, _type_list)

    @staticmethod
    def _get_sql_data_type(var_type: type) -> str:
        if var_type is int:
            return "INT"
        else:
            return "VARCHAR(255)"
        
    @staticmethod
    def _get_table_name(class_type: type | UniqueData) -> str:
        if not isinstance(class_type, str):
            if not isinstance(class_type, type):
                class_type = class_type.__class__
            class_type = class_type.__name__
        return str(class_type).lower()
        
    @staticmethod
    def _get_column_names(class_type: UniqueData):
        _headers = class_type.get_headers()
        return ', '.join(_headers)
        
    @staticmethod
    def _get_column_symbols(class_type: UniqueData):
        _headers = class_type.get_headers()
        _column_symbols = ['%s'] * len(_headers)
        return ', '.join(_column_symbols)





    @staticmethod
    def _get_column_definitions(class_type: UniqueData) -> str:
        _sql_definition_list = QueryGenerator._get_sql_definition_list(class_type)
        _sql_definition_list[0] = "%s UNIQUE" % (_sql_definition_list[0])
        return ', '.join(_sql_definition_list)
        
    @staticmethod
    def _get_sql_definition_list(class_type: UniqueData) -> str:
        _headers = class_type.get_headers()
        _types = QueryGenerator._get_sql_data_type_list(class_type)
        return ["%s %s" % (a, b) for a, b in zip(_headers, _types)]
        