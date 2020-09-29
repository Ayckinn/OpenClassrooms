# -*- coding: UTF-8 -*-

# ================================
# =   OFF Viewer : GUI VERSION   =
# = ==============================

import pathlib

from PyQt5 import QtWidgets, uic
from controller import Controller
from tools import constants as cst
from json.decoder import JSONDecodeError


class UIMode:

    def __init__(self):
        self.controller = Controller()
        self.app = QtWidgets.QApplication([])
        self.gui = uic.loadUi(".\\ui\\ui_mode.ui")

    def display_number_of_items(self):
        self.gui.nb_catg_lbl.setText(self.controller.display_number_of_categories_in_db())
        self.gui.nb_prod_lbl.setText(self.controller.display_number_of_products_in_db())

    def clear_list(self):
        self.gui.listWidget.clear()

    # -- BLOCK FOR CATEGORY MANAGEMENT --
    def add_categories(self):
        try:
            self.clear_list()
            self.controller.add_categories_in_db()
            self.gui.listWidget.addItem(cst.UI_UPDATE_OK)
            self.display_number_of_items()
        except JSONDecodeError:
            self.gui.listWidget.addItem(cst.URL_ERROR)

    def display_category_list(self):
        if self.controller.display_number_of_categories_in_db() == '0':
            self.clear_list()
            self.gui.listWidget.addItem(cst.EMPTY_CATEGORY_TABLE_UI)
        else:
            self.clear_list()
            for category in self.controller.get_all_items_in_category_table():
                self.gui.listWidget.addItem(str(category))

    # -- BLOCK FOR PRODUCT MANAGEMENT --
    def add_products(self):
        try:
            self.clear_list()
            self.controller.add_product_in_db()
            self.gui.listWidget.addItem(cst.UI_UPDATE_OK)
            self.display_number_of_items()
        except JSONDecodeError:
            self.gui.listWidget.addItem(cst.URL_ERROR)

    def display_product_list(self):
        if self.controller.display_number_of_products_in_db() == '0':
            self.clear_list()
            self.gui.listWidget.addItem(cst.EMPTY_PRODUCT_TABLE_UI)
        else:
            self.clear_list()
            for product in self.controller.get_all_items_in_product_table():
                self.gui.listWidget.addItem(str(product))

    def display_products_from_selected_category(self, item):
        self.category_id = item.text().strip("(").strip(")").split(",")[0]
        self.clear_list()
        for product in self.controller.get_products_by_category_id(self.category_id):
            self.gui.listWidget.addItem(str(product))

    def main(self):
        # -- BUTTONS EVENTS --
        self.gui.add_cat_btn.clicked.connect(self.add_categories)
        self.gui.dp_cat_btn.clicked.connect(self.display_category_list)
        self.gui.add_prod_btn.clicked.connect(self.add_products)
        self.gui.dp_prod_btn.clicked.connect(self.display_product_list)

        self.gui.cls_list_btn.clicked.connect(self.clear_list)
        self.gui.exit_btn.clicked.connect(self.gui.close)

        # -- DOUBLE CLICK ON SELECTED ITEM TO DISPLAY ASSOCIATED PRODUCTS --
        self.gui.listWidget.itemDoubleClicked.connect(self.display_products_from_selected_category)

        # -- LABEL EVENTS --
        self.display_number_of_items()

        self.gui.show()
        self.app.exec()


if __name__ == '__main__':
    if pathlib.Path(cst.FONT_PATH).is_file():
        print(cst.GREEN + "\n Font OK\n")
        UIMode().main()
    else:
        print(cst.RED + "\n Fonts are missing... "
                        "Please, install fonts contained in the [FONTS] folder.\n")
