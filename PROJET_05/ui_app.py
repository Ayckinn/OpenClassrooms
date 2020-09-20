# -*- coding: UTF-8 -*-

# ===========================================================
# =           OPEN FOOD FACTS DATABASE MANAGEMENT           =
# =               OPENCLASSROOMS - PROJECT 05               =
# =                                                         =
# =        Use publics datas from OpenFood Facts API        =
# =                 OFF Viewer : UI VERSION                 =
# = =========================================================

import pathlib

from tools import utils
from PyQt5 import QtWidgets, uic
from tools import constants as cst
from db_requests import db_products
from db_requests import db_categories
from json.decoder import JSONDecodeError

app = QtWidgets.QApplication([])
gui = uic.loadUi(".\\ui\\ui_mode.ui")
category_request = db_categories.Category()
product_request = db_products.Products()


# -- UI EVENTS --
def ui_mode():
	# -- Buttons events --
	gui.db_up_btn.clicked.connect(db_update)
	
	gui.cls_list_btn.clicked.connect(clear_list)
	gui.dp_cat_btn.clicked.connect(show_categories_list)
	gui.dp_prod_btn.clicked.connect(show_products_list)
	gui.exit_btn.clicked.connect(gui.close)

	# -- label events --
	gui.nb_catg_lbl.setText(str(len(category_request.db_column('id'))))
	gui.nb_prod_lbl.setText(str(len(product_request.db_column('id'))))

	gui.show()
	app.exec()


def db_update():
	try:
		clear_list()
		category_request.add_categories_in_db()
		product_request.add_products_in_db()
		gui.listWidget.addItem(" Database has been updated successfully...")
		gui.nb_catg_lbl.setText(str(len(category_request.db_column('id'))))
		gui.nb_prod_lbl.setText(str(len(product_request.db_column('id'))))
	except JSONDecodeError:
		gui.listWidget.addItem(cst.URL_ERROR)


def show_categories_list():
	if len(category_request.db_column('id')) == 0:  # -- If table is empty
		clear_list()
		gui.listWidget.addItem(cst.EMPTY_CATEGORIES_TABLE_MSG)
	else:
		clear_list()
		for category in category_request.db_column('*'):
			gui.listWidget.addItem(str(category))


def show_products_list():
	if len(product_request.db_column('id')) == 0:
		clear_list()
		gui.listWidget.addItem(cst.EMPTY_PRODUCTS_TABLE_MSG)
	else:
		clear_list()
		for product in product_request.db_column('*'):
			gui.listWidget.addItem(str(product))


def clear_list():
	gui.listWidget.clear()


if __name__ == '__main__':
	if pathlib.Path(cst.FONT_PATH).is_file():
		print(cst.GREEN + "\n Font OK\n")
		ui_mode()
	else:
		print(cst.RED + "\n Fonts are missing..."
			"Please, install fonts contained in the [FONTS] folder.\n")
