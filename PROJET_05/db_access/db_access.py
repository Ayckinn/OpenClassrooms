import os
import sys
import mysql.connector as mysql

from tools import constants as cst
from logo import logo


class DBcnx:
    """
    Module used for database access and management
    """

    def __init__(self):
        os.system('cls')

    def db_connect(self):
        try:
            dbconnect = mysql.connect(
                host = cst.DB_HOST,
                user = cst.DB_USERNAME,
                passwd = cst.DB_PASSWORD,
                database = cst.DB_NAME)
            logo.logo()

        except Exception:
            sys.exit(cst.RED + "\n /!\\ DATABASE ACCESS DENIED... "
            "Please retry later or check your login/password !\n" + cst.RESET)

        return dbconnect
