# This file is part of: github.com/pablocorbalann/secgenda
"""
The db handler contains the DataHandler class that is used to create all the cursors
and connections with the sql database.
"""
import sqlite3 as sql
from errors import DataError
import os


class DataHandler:
    """
    The data handler class is used to create the sql instances that
    are needed to use a SQL database, for example the connection
    and the SQL cursor.
    """
    def __init__(self, db_file):
        """
        The constructor method for the DataHandler file, it takes a parameter
        to stabilish the SQL connection.

        :param db_file: string -> the route of the file from the database
        """
        self.ROUTE = f"{db_file}.db"
        try:
            self.conn = sql.connect(self.ROUTE)
        except Exception as e:
            e_code = "005"
            e_message = "Can't create the SQL data connection"
            e = DataError(e_code, e, e_message)

    @property
    def cursor(self):
        """Creates the cursor for a query"""
        try:
            return self.conn.cursor()
        except Exception as e:
            e_code = "007"
            e_message = "We can't create a sql cursor in the handler"
            e = DataError(e_code, e, e_message)
            e.show()
        return -1 

def query(name):
    """
    This function is used for loading a SQL query from a file to the program,
    all the queries are located inside the q/ folder, in different files.

    secgenda/app/db/q/

    This function takes the name of the query file name :param name: and
    returns the query itself
    """
    try:
        path = os.path.abspath(f"app/db/q/{name}.sql")
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        # This is an internal error and can be really harmfull, so please
        # watch the typos :)
        e_code = "006"
        e_message = f"Can't find the query: '{name}', remember to run from the root"
        e = DataError(e_code, e, e_message)
        e.show()
    except Exception as e:
        e_code = "000"
        e = DataError(e_code, e)
        e.show()
