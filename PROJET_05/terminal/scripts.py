# ---------------------------------
# -- TERMINAL SCRIPTS MANAGEMENT --
# ---------------------------------

import time

from terminal import logo
from controller import Controller
from tools import constants as cst


class TerminalScript:

    def __init__(self):
        self.controller = Controller()

    def display_logo(self):
        logo.logo_connected()
        self.controller.get_number_of_categories_in_db()
        self.controller.get_number_of_products_in_db()

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
        if len(self.controller.get_number_of_items_in_id_column()) == 0:
            print(cst.MAGENTA + cst.EMPTY_CATEGORIES_TABLE_MSG)
            time.sleep(3)
            self.display_logo()
        else:
            print()
            for category in self.controller.get_all_items_in_category_table():
                self.loop_for_displaying_items(category)

    def user_choice_three(self):
        print(cst.CYAN + "\n You have chosen : Add products in database")
        print(cst.DB_UPDATE_IN_PROGRESS)
        self.controller.add_product_in_db()
        print(cst.DB_STATUS + cst.UPDATE_OK)
        time.sleep(3)
        self.display_logo()

    def user_choice_four(self):
        if len(self.controller.get_number_of_items_in_id_column()) == 0:
            print(cst.MAGENTA + cst.EMPTY_PRODUCTS_TABLE_MSG)
            time.sleep(3)
            self.display_logo()
        else:
            print()
            for product in self.controller.get_all_items_in_product_table():
                self.loop_for_displaying_items(product)

    def user_choice_five(self):
        try:
            if len(self.controller.get_number_of_items_in_id_column()) == 0:
                print(cst.MAGENTA + cst.EMPTY_PRODUCTS_TABLE_MSG)
                time.sleep(3)
                self.display_logo()
            else:
                user_select = int(input("\n Choose a category by ID : "))
                print()
                if user_select > len(self.controller.get_number_of_items_in_id_column()):
                    print(cst.RED + cst.EXCEED_DB_CATEGORY_ID)
                for product in self.controller.get_products_by_category_id(user_select):
                    self.loop_for_displaying_items(product)
                print()
        except ValueError:
            print(cst.RED + "\n Please, select by category ID, letters are not allowed...")
