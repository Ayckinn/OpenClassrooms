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
from db_requests import products
from db_requests import categories
from tools import constants as cst
from json.decoder import JSONDecodeError

app = QtWidgets.QApplication([])
ui_view = uic.loadUi(".\\ui\\ui_db_view.ui")
category_request = categories.Category()
product_request = products.Products()


def db_ui_view():
	# -- Buttons events --
	#ui_view.db_up_btn.clicked.connect(db_update)
	ui_view.dp_cat_btn.clicked.connect(categories_list)
	ui_view.dp_prod_btn.clicked.connect(products_list)
	ui_view.exit_btn.clicked.connect(ui_view.close)

	# -- label events --
	ui_view.nb_catg_lbl.setText(str(len(category_request.db_column('id'))))
	ui_view.nb_prod_lbl.setText(str(len(product_request.db_column('id'))))

	ui_view.show()
	app.exec()


def show_list(table):
	ui_view.tableWidget.setRowCount(0)

	for row_number, row_data in enumerate (table.db_column('*')):
		ui_view.tableWidget.insertRow(row_number)
		for column_number, column_data in enumerate (row_data):
			ui_view.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))


def categories_list():
	show_list(category_request)

def products_list():
	show_list(product_request)

def clear_list():
	ui_view.tableWidget.clear()


if __name__ == '__main__':
	if pathlib.Path(cst.FONT_PATH).is_file():
		print(cst.GREEN + "\n Font OK\n")
		db_ui_view()
	else:
		print(cst.RED + "\n Fonts are missing..."
			"Please, install fonts contained in the [FONTS] folder.\n")