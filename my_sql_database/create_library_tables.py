from typing import List, Tuple
import mysql.connector


class CreateLibraryTables:
    def create_table(self, _table_name: str, column_names: list[str], column_types: list[str],
                     library_data: list[Tuple], database_connector: mysql.connector.MySQLConnection) -> None:
        
        try:
            # Connect to the database
            with database_connector.cursor() as cursor:
                
                # Link data names with data types
                column_definitions = ["%s %s" % (col_name, col_type) for col_name, col_type in zip(column_names, column_types)]
                column_definitions_combined = ', '.join(column_definitions)
                create_table_query = "CREATE TABLE IF NOT EXISTS %s (%s)" % (_table_name, column_definitions_combined)
                cursor.execute(create_table_query)

                _column_names_combined = ', '.join(column_names)
                _column_symbols = ['%s'] * len(column_names)
                _column_symbols_combined = ', '.join(_column_symbols)
                insert_query = "INSERT INTO %s (%s) VALUES (%s)" % (_table_name, _column_names_combined, _column_symbols_combined)

                cursor.executemany(insert_query, library_data)

            # Commit changes
            database_connector.commit()

            print("Table %s created successfully." % (_table_name))
        except mysql.connector.Error as e:
            print("Error creating table: %s" % (e))
            raise