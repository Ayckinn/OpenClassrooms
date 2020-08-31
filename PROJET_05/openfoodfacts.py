# -*- coding: UTF-8 -*-

# ===========================================================
# =            OPEN FOOD FACTS DATABASE HANDLING            =
# =               OPENCLASSROOMS - PROJECT 05               =
# =                                                         =
# =    Use publics datas from OpenFood Facts API            =
# = =========================================================


import sys
import ui_app
import terminal_app

from tools import logo
from tools import constants as cst


def main():
	loop = True

	try:
		while loop:
			logo.logo_connected()

			print(""" Choose a view mode :

		 [1]  \033[1;36mTerminal Interface mode\033[0;m
		 [2]  \033[1;36mGraphical User Interface mode\033[0;m

		 [0x] \033[1;36mExit\033[0;m\n""")

			user_choice = input(cst.CYAN + " >> " + cst.RESET)

			if user_choice == "1":
				terminal_app.terminal_mode()
			elif user_choice == "2":
				ui_app.ui_mode()
			elif user_choice == "0x":
				sys.exit(cst.BLUE + "\n Program exit... See you soon ^^\n")

	except KeyboardInterrupt:
		sys.exit("\n\n" + cst.RED +" Program killed by user..\n")


if __name__ == "__main__":
	main()