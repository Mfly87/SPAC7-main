from dataClasses import UniqueData
from dataClasses.dataTypes import Category
from .query_generator import QueryGenerator

from mysql.connector import MySQLConnection, Error
class CreateLibraryTables:
    def create_table(self, database_connector: MySQLConnection, unique_data_list: list[UniqueData]) -> None:
        

        if not unique_data_list:
            return
        
        class_type = type(unique_data_list[0])

        _gen = QueryGenerator()
        
        try:
            with database_connector.cursor() as cursor:
                _drop_table = _gen.drop_table_for_class(class_type)
                cursor.execute(_drop_table)
            database_connector.commit()
        except:
            pass
        #_gen.generate_search_query(Category)
        try:
            # Connect to the database
            with database_connector.cursor() as cursor:

                _create_table_query = _gen.generate_table_for_class(class_type)
                print(_create_table_query)
                cursor.execute(_create_table_query)

                library_data = []
                for _unique_data in unique_data_list:
                    library_data.append(tuple(_unique_data.to_list()))

                insert_query = _gen.generate_insertion_query(class_type)
                cursor.executemany(insert_query, library_data)

            # Commit changes
            database_connector.commit()



        except Error as e:
            print("Error creating table: %s" % (e))
            raise

    def search(self, database_connector: MySQLConnection, class_type: UniqueData | type,*, search_term: str = ""):
        
        _gen = QueryGenerator()
        with database_connector.cursor(dictionary = True) as cursor:
            _search_qeary = _gen.generate_search_query(class_type, search_term = search_term)
            print(_search_qeary)
            cursor.execute(_search_qeary)
            return cursor.fetchall()
        
    def update(self, database_connector: MySQLConnection, unique_data: UniqueData):
        _gen = QueryGenerator()
        _query = _gen.generate_update_query(unique_data)
        print(_query)
        
        with database_connector.cursor() as cursor:
            cursor.execute(_query)
        database_connector.commit()
        