# -*- coding: UTF-8 -*-

# ===========================================================
# =            OPEN FOOD FACTS DATABASE HANDLING            =
# =               OPENCLASSROOMS - PROJECT 05               =
# =                                                         =
# =        Use publics datas from OpenFood Facts API        =
# =                 OFF Viewer : UI VERSION                 =
# = =========================================================


import pathlib

from tools import constants as cst
from PyQt5 import QtWidgets, uic
from db_requests import categories

CATG_RQ = categories.Category()
APP_WINDOW = QtWidgets.QApplication([])
UI = uic.loadUi(".\\ui\\ui_mode.ui")
ADD_ITEM = UI.listWidget.addItem


# -- UI EVENTS --
def ui_mode():
	# -- Buttons events --
	UI.db_up_btn.clicked.connect(db_update)
	UI.dp_cat_btn.clicked.connect(show_list)
	UI.cls_list_btn.clicked.connect(clear_list)
	UI.exit_btn.clicked.connect(UI.close)
	UI.refresh_db_btn.clicked.connect(refresh_db)

	# -- label events --
	nb_catg_txt()

	UI.show()
	APP_WINDOW.exec()


def db_update():
	clear_list()
	ADD_ITEM("\n Database update in progress... Please, wait...")
	CATG_RQ.create_category_table()
	ADD_ITEM(" Database has been updated successfully...")
	nb_catg_txt()


def show_list():
	if len(CATG_RQ.check_category_table()) == 0:  # -- If table is empty
		clear_list()
		ADD_ITEM("\n Categories table is empty !")
	else:
		clear_list()
		for catg in CATG_RQ.show_category_list():
			ADD_ITEM(str(catg))


def clear_list():
	UI.listWidget.clear()


def nb_catg_txt():
	UI.nb_catg_lbl.setText(str(len(CATG_RQ.check_category_table())))


def refresh_db():
    clear_list()
    ADD_ITEM("\n Database has been refreshed...")

    nb_catg_txt()
    
    if len(CATG_RQ.check_category_table()) == 0:  # -- If table is empty
        ADD_ITEM("\n Categories table is empty !")
    else:
    	for catg in CATG_RQ.show_category_list():
    		ADD_ITEM((str(catg)))


if __name__ == '__main__':
	if pathlib.Path(cst.FONT_PATH).is_file():
		print(cst.GREEN + "\n Font OK\n")
		ui_mode()
	else:
		print(cst.RED + "\n Fonts are missing... Please, install fonts contained in the [FONTS] folder.\n")
