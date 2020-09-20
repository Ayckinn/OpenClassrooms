# -*- coding: UTF-8 -*-

# ===========================================================
# =           OPEN FOOD FACTS DATABASE MANAGEMENT           =
# =               OPENCLASSROOMS - PROJECT 05               =
# =                                                         =
# =        Use publics datas from OpenFood Facts API        =
# =              OFF Viewer - TERMINAL VERSION              =
# = =========================================================

import sys
import time
import ui_app

from term import logo
from tools import utils
from term import terminal_list
from tools import constants as cst
from db_requests import db_products
from db_requests import db_categories
from json.decoder import JSONDecodeError

categories_in_db = db_categories.Category()
product_request = db_products.Products()
terminal_list_options = terminal_list.TerminalListOptions()


def display_logo():
    logo.logo_connected()
    categories_in_db.show_categories_number_in_db()
    product_request.show_products_number_in_db()


def terminal_mode():
    loop = True
    try:
        try:
            display_logo()
            try:
                while loop:
                    terminal_list_options.print_list()
                    user_choice = input(cst.CYAN + " >> " + cst.WHITE)

                    if user_choice == "1":
                        print(cst.CYAN + "\n Add categories...")
                        print(" Database update in progress.. Please wait....")
                        categories_in_db.add_categories_in_db()
                        print(cst.DB_STATUS + cst.UPDATE_OK)
                        categories_in_db.show_categories_number_in_db()
                        product_request.show_products_number_in_db()

                    elif user_choice == "2":
                        if len(categories_in_db.db_column('id')) == 0:
                            print(cst.MAGENTA + cst.EMPTY_CATEGORIES_TABLE_MSG)
                            time.sleep(3)
                            display_logo()
                        else:
                            print()
                            for category in categories_in_db.db_column('*'):
                                utils.teminal_loop_for_displaying_items(category, cst.YELLOW, cst.BLUE)
                            print()

                    elif user_choice == "3":
                        print(cst.CYAN + "\n Add products...")
                        print(" Database update in progress.. Please wait....")
                        product_request.add_products_in_db()
                        print(cst.DB_STATUS + cst.UPDATE_OK)
                        categories_in_db.show_categories_number_in_db()
                        product_request.show_products_number_in_db()

                    elif user_choice == "4":
                        if len(product_request.db_column('id')) == 0:
                            print(cst.MAGENTA + cst.EMPTY_PRODUCTS_TABLE_MSG)
                            time.sleep(3)
                            display_logo()
                        else:
                            print()
                            for product in product_request.db_column('*'):
                                utils.teminal_loop_for_displaying_items(product, cst.CYAN, cst.MAGENTA)
                            print()

                    elif user_choice == "5":
                        try:
                            if len(product_request.db_column('id')) == 0:
                                print(cst.MAGENTA + cst.EMPTY_PRODUCTS_TABLE_MSG)
                                time.sleep(3)
                                display_logo()
                            else:
                                user_select = int(input("\n Choose a category by ID : "))
                                print()
                                for product in product_request.display_products_for_a_category(user_select):
                                    utils.teminal_loop_for_displaying_items(product, cst.RED, cst.WHITE)
                                print()
                        except ValueError:
                            print(cst.RED + "\n Please, select by category ID, letters are not allowed...")

                    elif user_choice == "i":
                        ui_app.ui_mode()
                    elif user_choice == "c":
                        logo.logo_connected()
                        categories_in_db.show_categories_number_in_db()
                        product_request.show_products_number_in_db()
                    elif user_choice == "x":
                        sys.exit(cst.EXIT_MSG)
                    else:
                        print(cst.WRONG_CHOICE + "\n")

            except KeyboardInterrupt:
                sys.exit("\n\n" + cst.KILLED_MSG)
        except KeyboardInterrupt:
            sys.exit("\n\n" + cst.KILLED_MSG)
    except JSONDecodeError:
        print(cst.URL_ERROR)


if __name__ == '__main__':
    terminal_mode()
