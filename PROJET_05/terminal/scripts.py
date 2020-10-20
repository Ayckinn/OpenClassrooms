# ---------------------------------
# -- TERMINAL SCRIPTS MANAGEMENT --
# ---------------------------------

import time

from terminal.logo import Logo
from controller import Controller
from tools import constants as cst


class TerminalScript:
    """ This class allows to manage all functions for terminal view """

    def __init__(self):
        self.controller = Controller()
        self.logo = Logo()

    def display_logo(self):
        self.logo.logo_connected()
        self.controller.get_number_of_categories_in_db()
        self.controller.get_number_of_products_in_db()
        self.controller.get_number_of_favorite_in_db()

    def loop_for_displaying_items(self, table):
        for line in table:
            print(cst.GREEN + (str(line)), end = " | ")
        print()
        for _ in range(125):
            print(cst.BLUE + ".", end = "")
        print()

    # ===== USER CHOICE MANAGEMENT BLOCK =====
    def user_choice_one(self):
        print(cst.CYAN + "\n You have chosen : Add categories in database")
        print(cst.DB_UPDATE_IN_PROGRESS)
        self.controller.add_categories_in_db()
        print(cst.DB_STATUS + cst.UPDATE_OK)
        time.sleep(3)
        self.display_logo()

    def user_choice_two(self):
        if len(self.controller.get_items_in_category_table('id')) == 0:
            print(cst.EMPTY_CATEGORY_TABLE_MSG)
            time.sleep(3)
            self.display_logo()
        else:
            print()
            for category in self.controller.get_items_in_category_table('*'):
                self.loop_for_displaying_items(category)
            print()

    def user_choice_three(self):
        print(cst.CYAN + "\n You have chosen : Add products in database")
        print(cst.DB_UPDATE_IN_PROGRESS)
        self.controller.add_product_in_db()
        print(cst.DB_STATUS + cst.UPDATE_OK)
        time.sleep(3)
        self.display_logo()

    def user_choice_four(self):
        if len(self.controller.get_items_in_category_table('id')) == 0:
            print(cst.EMPTY_PRODUCT_TABLE_MSG)
            time.sleep(3)
            self.display_logo()
        else:
            print()
            for product in self.controller.get_items_in_product_table('*'):
                self.loop_for_displaying_items(product)
            print()

    def user_choice_five(self):
        try:
            if len(self.controller.get_items_in_category_table('id')) == 0:
                print(cst.MAGENTA + cst.EMPTY_CATEGORY_TABLE_MSG)
                time.sleep(3)
                self.display_logo()
            else:
                user_select = int(input("\n Choose a category by ID : "))
                print()
                if user_select > len(self.controller.get_items_in_category_table('id')):
                    print(cst.EXCEED_DB_CATEGORY_ID)
                for product in self.controller.get_products_by_category_id(user_select):
                    self.loop_for_displaying_items(product)
                print()
        except ValueError:
            print(cst.RED + "\n Please, select by category ID, letters are not allowed...")

    def user_choice_six(self):
        try:
            if len(self.controller.get_items_in_product_table('id')) == 0:
                print(cst.MAGENTA + cst.EMPTY_PRODUCT_TABLE_MSG)
                time.sleep(3)
                self.display_logo()
            else:
                user_select = int(input("\n Choose a product by ID : "))
                print()
                if user_select > len(self.controller.get_items_in_product_table('id')):
                    print(cst.EXCEED_DB_PRODUCT_ID)
                else:
                    product = self.controller.get_product_by_id(user_select)
                    self.controller.add_product_in_favorite(product[0])
                print()
        except ValueError:
            print(cst.RED + "\n Please, select by category ID, letters are not allowed...")

    def user_choice_seven(self):
        if len(self.controller.get_items_in_favorite_table('id')) == 0:
            print(cst.EMPTY_FAVORITE_TABLE_MSG)
            time.sleep(3)
            self.display_logo()
        else:
            print()
            for fav in self.controller.get_items_in_favorite_table('*'):
                self.loop_for_displaying_items(fav)
            print()

    def delete_database(self):
        self.controller.delete_database()
        print(" Database has been deleted successfully..")
        time.sleep(3)
        self.display_logo()
