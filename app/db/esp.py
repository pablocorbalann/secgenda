# This file is part of: github.com/pablocorbalann/secgenda
"""
The esp.py module (short from specific.py) contains all the functions that are used to
check if specific things are working in the SQL database, for example it may check if a
contact is valid.

For more information check out the github repository: github.com/pablocorbalann/secgenda
"""
from .handler import query

def setup_table(dh):
    """
    This function is used to setup a table using a given
    data handler :param dh:
    """
    q_name = "make_table"
    q = query(q_name)
    dh.cursor.execute(q)
    dh.conn.commit()
