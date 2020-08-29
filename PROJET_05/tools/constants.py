# --------------------------------------------
# -- MODULE CONTAINING CONSTANTS OF PROJECT --
# --------------------------------------------


import pathlib
import colorama

from colorama import Fore

colorama.init(autoreset=True)


# -- DATABASE CONSTANTS
DB_HOST = 'localhost'
DB_USERNAME = 'username'
DB_PASSWORD = 'password'
DB_NAME = 'openfoodfacts'

# -- TABLES CONSTANTS
CATG_TABLE = 'categories'
PROD_TABLE = 'products'
FAV_TABLE = 'favorites'

# -- FONTS COLOR
GREEN = Fore.GREEN
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.YELLOW
WHITE = Fore.WHITE
RESET = Fore.RESET

# -- UI MODE
USER_DIR = str(pathlib.Path.home())
FONT_PATH = (USER_DIR + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Failed-3d-Filled.ttf")