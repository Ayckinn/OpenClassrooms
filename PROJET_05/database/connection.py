# --------------------------------
# -- DATABASE ACCESS MANAGEMENT --
# --------------------------------

import os
import sys

from terminal import logo
from tools import constants as cst
from mysql import connector as mysql


class DBConnection:
    """
    Module used for connection to database
    """

    def __init__(self):
        self.is_connected = False
        self.dbconnect = None

    def connect(self):
        try:
            self.dbconnect = mysql.connect(
                host = cst.DB_HOST,
                user = cst.DB_USERNAME,
                passwd = cst.DB_PASSWORD,
                database = cst.DB_NAME)
            self.is_connected = True

        except Exception:
            sys.exit(logo.logo_not_connected())

        return self.dbconnect

    def get_db_connection(self):
        return self.dbconnect
