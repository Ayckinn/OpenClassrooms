# --------------------------------
# -- DATABASE ACCESS MANAGEMENT --
# --------------------------------


import os
import sys

from tools import logo
from tools import constants as cst
from mysql import connector as mysql


class DBcnx:
    """
    Module used for database access and management
    """

    def __init__(self):
        os.system('cls')
        

    def db_connect(self):
        logo.logo()

        try:
            dbconnect = mysql.connect(
                host = cst.DB_HOST,
                user = cst.DB_USERNAME,
                passwd = cst.DB_PASSWORD,
                database = cst.DB_NAME)

        except Exception:
            sys.exit(logo.logo_not_connected())

        return dbconnect
