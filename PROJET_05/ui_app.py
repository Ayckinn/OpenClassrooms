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


def clicked():
	print("Update done !")


def ui_mode():
	app_window = QtWidgets.QApplication([])
	design = uic.loadUi(".\\ui\\ui_mode.ui")

	design.db_up_btn.clicked.connect(clicked)

	design.show()
	app_window.exec()


if __name__ == '__main__':
	if pathlib.Path(cst.FONT_PATH).is_file():
		print(cst.GREEN + "\n Font OK\n")
		ui_mode()
	else:
		print(cst.RED + "\n Fonts are missing... Please, install fonts contained in the [FONTS] folder.\n")
