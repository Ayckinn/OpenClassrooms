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
from db_requests import products
from db_requests import categories
from tools import constants as cst
from json.decoder import JSONDecodeError

category_request = categories.Category()
product_request = products.Products()
terminal_list_options = terminal_list.TerminalListOptions()


def display_logo():
    logo.logo_connected()
    category_request.show_categories_number_in_db()
    product_request.show_products_number_in_db()


def terminal_mode():
    loop = True
    try:
        try:
            display_logo()
            
            user_response = input("\n Do you want to update database (y/n) : ").lower()
            if user_response == 'y':
                print("\n Database update in progress.. Please wait....")
                category_request.add_categories_in_db()
                time.sleep(2)
                product_request.add_products_in_db()
                display_logo()
                print(cst.DB_STATUS + cst.UPDATE_OK)

            elif user_response == 'n':
                print(cst.DB_STATUS + cst.UPDATE_NOK)
            else:
                sys.exit(cst.WRONG_CHOICE)

            try:
                while loop:
                    terminal_list_options.print_list()
                    user_choice = input(cst.CYAN + " >> " + cst.WHITE)

                    if user_choice == "1":
                        print("\n Database update in progress.. Please wait....")
                        category_request.add_categories_in_db()
                        print(cst.DB_STATUS + cst.UPDATE_OK)
                        category_request.show_categories_number_in_db()
                        product_request.show_products_number_in_db()

                    elif user_choice == "2":
                        if len(category_request.db_column('id')) == 0:
                            print(cst.MAGENTA + cst.EMPTY_CATEGORIES_TABLE_MSG)
                            time.sleep(3)
                            display_logo()
                        else:
                            print()
                            for category in category_request.db_column('*'):
                                utils.teminal_loop_for_displaying_items(category, cst.YELLOW, cst.BLUE)
                            print()

                    elif user_choice == "3":
                        if len(product_request.db_column('id')) == 0:
                            print(cst.MAGENTA + cst.EMPTY_PRODUCTS_TABLE_MSG)
                            time.sleep(3)
                            display_logo()
                        else:
                            print()
                            for product in product_request.db_column('*'):
                                utils.teminal_loop_for_displaying_items(product, cst.CYAN, cst.MAGENTA)
                            print()

                    elif user_choice == "4":
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

                    # ////////////////////////////// JUST FOR TEST //////////////////////////////
                    elif user_choice == "t":
                        product_request.add_products_in_db()
                        print(cst.DB_STATUS + cst.UPDATE_OK)
                        category_request.show_categories_number_in_db()
                        product_request.show_products_number_in_db()
                    # ///////////////////////////////////////////////////////////////////////////

                    elif user_choice == "i":
                        ui_app.ui_mode()
                    elif user_choice == "c":
                        logo.logo_connected()
                        category_request.show_categories_number_in_db()
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