# --------------------------------------------
# -- MODULE CONTAINING CONSTANTS OF PROJECT --
# --------------------------------------------


import pathlib
import colorama

from colorama import Fore

colorama.init(autoreset = True)


# -- GENERAL CONSTANTS --
CATEGORIES_JSON_URL = "https://fr.openfoodfacts.org/categories.json"


# -- DATABASE CONSTANTS --
DB_HOST 	= 'localhost'
DB_USERNAME = 'ayckinn'
DB_PASSWORD = 'marlene'
DB_NAME 	= 'openfoodfacts'


# -- TABLES CONSTANTS --
CATEGORY_TABLE 	= 'category'
PRODUCT_TABLE 	= 'product'
FAV_TABLE 		= 'favorite'


# -- FONTS COLOR --
GREEN 	= Fore.GREEN
CYAN 	= Fore.CYAN
MAGENTA = Fore.MAGENTA
BLUE 	= Fore.BLUE
RED 	= Fore.RED
YELLOW 	= Fore.LIGHTYELLOW_EX
WHITE 	= Fore.WHITE
RESET 	= Fore.RESET


# -- UI MODE --
USER_DIR 	 			 = str(pathlib.Path.home())
FONT_PATH 	 			 = (USER_DIR + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Failed-3d-Filled.ttf")
UI_UPDATE_OK 			 = "Database has been updated successfully..."
EMPTY_CATEGORY_TABLE_UI  = "Categories table is empty..."
EMPTY_PRODUCT_TABLE_UI 	 = "Products table is empty..."


# -- TERMINAL MODE --
DB_STATUS 				 = MAGENTA + "\n DATABASE STATUS => "
UPDATE_OK 				 = GREEN + "DATABASE HAS BEEN UPDATED SUCCESSFULLY..."
UPDATE_NOK 				 = RED + "DATABASE NOT UPDATED !"
URL_ERROR 				 = RED + "\n UPDATE ERROR !! URL DOWN...\n"
KILLED_MSG 				 = RED + " Program killed by user..\n"
EXIT_MSG 				 = BLUE + "\n Program exit... See you soon ^^\n"
WRONG_CHOICE_Y_N 		 = RED + "\n WRONG CHOICE ! Please, select with 'y' or 'n'.\n"
WRONG_CHOICE_LIST 		 = RED + "\n WRONG CHOICE ! Please, select an option in the list..."
EMPTY_CATEGORY_TABLE_MSG = MAGENTA + "\n Categories table is empty..."
EMPTY_PRODUCT_TABLE_MSG  = MAGENTA + "\n Products table is empty..."
DB_UPDATE_IN_PROGRESS 	 = " Database update in progress... Please wait..."
EXCEED_DB_CATEGORY_ID 	 = RED + " The number you have chosen exceeds the number of categories in the database..."
