import os
import sys
import colorama

import mysql.connector as mysql
from colorama import Fore

colorama.init()

def db_connect():
    os.system('cls')

    try:
        dbconnect = mysql.connect(
            host = 'localhost',
            user = 'ayckinn',
            passwd = 'marlene',
            database = 'openfoodfact')
    except Exception:
        sys.exit(Fore.RED + "\n /!\\ DATABASE ACCESS DENIED... Please retry later or check your login/password !\n")

    return dbconnect