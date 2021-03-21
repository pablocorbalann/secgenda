# This file is part of: github.com/pablocorbalann/secgenda
"""
The db handler contains the DataHandler class that is used to create all the cursors
and connections with the sql database.
"""
import sqlite3 as sql
from errors import DataError
import os

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
        e_code = "006"
        e_message = f"Can't find the query: '{name}', remember to run from the root"
        e = DataError(e_code, e, e_message)
        e.show()
    except Exception as e:
        e_code = "000"
        e = DataError(e_code, e)
        e.show()

class DataHandler:
    def __init__(self, db_file):
        self.ROUTE = f"{db_file}.db"
        try:
            self.conn = sql.connect(self.ROUTE)
            self.cursor = self.conn.cursor()
        except Exception as e:
            e_code = "005"
            e_message = "Can't create the SQL data connection or cursor"
            e = DataError(e_code, e, e_message)


