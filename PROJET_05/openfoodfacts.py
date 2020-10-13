# -*- coding: UTF-8 -*-

# ===========================================================
# =            OPEN FOOD FACTS DATABASE HANDLING            =
# =        Use publics datas from OpenFood Facts API        =
# =                                                         =
# =    ©2020 Yannick HEUDE - OpenClassrooms : Project 05    =
# = =========================================================

import sys
import time

from ui_app import UIMode
from terminal.logo import Logo
from tools import constants as cst
from terminal_app import TerminalMode
from terminal.scripts import TerminalScript


class OffApp:

    def __init__(self):
        self.loop = True
        self.logo = Logo()
        self.ui = UIMode()
        self.terminal = TerminalMode()
        self.terminal_script = TerminalScript()

    def main(self):
        self.logo.neutral_logo()
        try:
            while self.loop:
                self.terminal_script.display_logo()

                print(""" Please, choose a view app :
                
  [1] \033[1;34mTerminal Interface mode\033[0;m
  [2] \033[1;34mGraphical User Interface mode\033[0;m

  [x] \033[1;32mExit\033[0;m\n""")

                user_choice = input(cst.YELLOW + " >> " + cst.RESET).lower()

                if user_choice == "1":
                    self.terminal.main()
                elif user_choice == "2":
                    self.ui.main()
                elif user_choice == "x":
                    sys.exit(cst.EXIT_MSG)
                else:
                    print(cst.WRONG_CHOICE_LIST)
                    time.sleep(3)

        except KeyboardInterrupt:
            sys.exit("\n" + cst.KILLED_MSG)


if __name__ == "__main__":
    print(cst.LOADING_DB_MSG)
    OffApp().main()
