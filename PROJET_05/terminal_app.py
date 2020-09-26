# -*- coding: UTF-8 -*-

# ===========================================================
# =           OPEN FOOD FACTS DATABASE MANAGEMENT           =
# =               OPENCLASSROOMS - PROJECT 05               =
# =                                                         =
# =        Use publics datas from OpenFood Facts API        =
# =              OFF Viewer - TERMINAL VERSION              =
# = =========================================================

import sys

from controller import Controller
from tools import constants as cst
from json.decoder import JSONDecodeError
from terminal.scripts import TerminalScript
from terminal.terminal_list import ListOptions


class TerminalMode:

    def __init__(self):
        self.controller = Controller()
        self.terminal_list = ListOptions()
        self.terminal_script = TerminalScript()

    def main(self):
        loop = True
        try:
            try:
                self.terminal_script.display_logo()
                try:
                    while loop:
                        self.terminal_list.print_list()
                        user_choice = input(cst.CYAN + " >> " + cst.WHITE)

                        if user_choice == "1":
                            self.terminal_script.user_choice_one()
                        elif user_choice == "2":
                            self.terminal_script.user_choice_two()
                        elif user_choice == "3":
                            self.terminal_script.user_choice_three()
                        elif user_choice == "4":
                            self.terminal_script.user_choice_four()
                        elif user_choice == "5":
                            self.terminal_script.user_choice_five()
                        elif user_choice == "i":
                            pass
                        elif user_choice == "c":
                            self.terminal_script.display_logo()
                        elif user_choice == "x":
                            sys.exit(cst.EXIT_MSG)
                        else:
                            print(cst.WRONG_CHOICE_LIST + "\n")

                except KeyboardInterrupt:
                    sys.exit("\n\n" + cst.KILLED_MSG)
            except KeyboardInterrupt:
                sys.exit("\n\n" + cst.KILLED_MSG)
        except JSONDecodeError:
            print(cst.URL_ERROR)


if __name__ == "__main__":
    TerminalMode().main()
