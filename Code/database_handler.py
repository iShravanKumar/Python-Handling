import mysql.connector
from log_generator import logging


class DB_CONNECTION:

    def __init__(self):
        self.database_connection = None

    @staticmethod
    def establish_connection(user, password):
        try:
            conn = mysql.connector.connect(host="localhost", user=user, password=password)  # "Vvu8z9D"
            return conn, True
        except mysql.connector.Error as error:
            logging.debug(f"MySQL Error during Connection {error}")
            return None, False
        except Exception as error:
            logging.debug(f"Unknown Error {error}")
            return None, False


class CRUD(DB_CONNECTION):
    def __init__(self):
        DB_CONNECTION.__init__(self)
        # self.database_connection, self.check = DB_CONNECTION.establish_connection('shravan', 'Vvu8z9D')

    @staticmethod
    def create_table(database_connection, database_name, table_name, create_command):
        try:
            database_cursor = database_connection.cursor()
            database_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            database_cursor.execute(f"DROP TABLE IF EXISTS {database_name}.{table_name}")
            database_cursor.execute(create_command)
            database_connection.commit()
            return True
        except mysql.connector.Error as error:
            logging.debug(f"MySQL Error during CREATE {error}")
            return False
        except Exception as error:
            logging.debug(f"Unknown Error {error}")
            return False

    @staticmethod
    def insert_values(database_connection, database_name, table_name, insert_command, insert_values):
        try:
            database_cursor = database_connection.cursor()
            database_cursor.executemany(insert_command, insert_values)
            database_connection.commit()
            return True
        except mysql.connector.Error as error:
            logging.debug(f"MySQL Error during INSERT {error}")
            return False
        except Exception as error:
            logging.debug(f"Unknown Error {error}")
            return False

    @staticmethod
    def update_values(database_connection, database_name, table_name, update_command, update_values):
        try:
            database_cursor = database_connection.cursor()
            database_cursor.executemany(update_command, update_values)
            database_connection.commit()
            return True
        except mysql.connector.Error as error:
            logging.debug(f"MySQL Error during UPDATE {error}")
            return False
        except Exception as error:
            logging.debug(f"Unknown Error {error}")
            return False

    @staticmethod
    def delete_rows(database_connection, database_name, table_name, delete_command):
        try:
            database_cursor = database_connection.cursor()
            database_cursor.execute(delete_command)
            database_connection.commit()
            return True
        except mysql.connector.Error as error:
            logging.debug(f"MySQL Error during CREATE {error}")
            return False
        except Exception as error:
            logging.debug(f"Unknown Error {error}")
            return False
