# --------------------------------------------
# -- MODULE CONTAINING CONSTANTS OF PROJECT --
# --------------------------------------------


import pathlib
import colorama

from colorama import Fore
from db_access import db_access

colorama.init(autoreset=True)


# -- GENERAL CONSTANTS --
CATEGORIES_JSON_URL = "https://fr.openfoodfacts.org/categories.json"


# -- DATABASE CONSTANTS --
DB_HOST = 'localhost'
DB_USERNAME = 'ayckinn'
DB_PASSWORD = 'marlene'
DB_NAME = 'openfoodfacts'


# -- TABLES CONSTANTS --
CATEGORIES_TABLE = 'categories'
PRODUCTS_TABLE = 'products'
FAV_TABLE = 'favorites'


# -- FONTS COLOR --
GREEN = Fore.GREEN
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.LIGHTYELLOW_EX
WHITE = Fore.WHITE
RESET = Fore.RESET


# -- UI MODE --
USER_DIR = str(pathlib.Path.home())
FONT_PATH = (USER_DIR + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Failed-3d-Filled.ttf")


# -- TERMINAL MODE --
DB_STATUS = MAGENTA + "\n DATABASE STATUS => "
UPDATE_OK = GREEN + "DATABASE HAS BEEN UPDATED SUCCESSFULLY..."
UPDATE_NOK = RED + "DATABASE NOT UPDATED !"
URL_ERROR = RED + "\n UPDATE ERROR !! URL DOWN...\n"
KILLED_MSG = RED + " Program killed by user..\n"
EXIT_MSG = BLUE + "\n Program exit... See you soon ^^\n"
WRONG_CHOICE = RED + "\n WRONG CHOICE ! Please, select with 'y' or 'n'.\n"
EMPTY_CATEGORIES_TABLE_MSG = "\n Categories table is empty..."
EMPTY_PRODUCTS_TABLE_MSG = "\n Products table is empty..."
