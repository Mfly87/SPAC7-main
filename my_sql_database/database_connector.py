from design_patterns import Singleton
import mysql.connector


class ConnectToDatabase(Singleton):
    def connect_to_server(self) -> mysql.connector:
        try:
            # Connect to the server
            my_database = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Kom12345",
                port=3306
            )
            return my_database
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    def connect_to_database(self, database_name: str) -> mysql.connector.connection.MySQLConnection:
        try:
            # Connect to the specified server
            my_database = self.connect_to_server()

            # Check if the database exists
            cursor = my_database.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

            # Switch to the specified database
            cursor.execute(f"USE {database_name}")
            cursor.close()  # Close the cursor after switching the database

            return my_database
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise
