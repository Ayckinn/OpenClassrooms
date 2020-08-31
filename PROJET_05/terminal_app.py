# -*- coding: UTF-8 -*-

# ===========================================================
# =            OPEN FOOD FACTS DATABASE HANDLING            =
# =               OPENCLASSROOMS - PROJECT 05               =
# =                                                         =
# =        Use publics datas from OpenFood Facts API        =
# =              OFF Viewer - TERMINAL VERSION              =
# = =========================================================


import sys
import time
import ui_app

from tools import logo
from tools import constants as cst
from db_requests import categories

CATG_RQ = categories.Category()


def terminal_mode():
    loop = True
    
    try:
        logo.logo_connected()

        user_response = input(" \n Do you want to update database (y/n) : ").lower()
        if user_response == 'y':
            CATG_RQ.create_category_table()
            print(cst.MAGENTA + "\n DATABASE STATUS => " 
                + cst.GREEN + "DATABASE HAS BEEN UPDATED SUCCESSFULLY...")
            print(cst.YELLOW + "\n There are " + cst.CYAN 
                + f"{len(CATG_RQ.check_category_table())}" 
                + cst.YELLOW + " categories in database.")
        
        elif user_response == 'n':
            print(cst.MAGENTA + "\n DATABASE STATUS => " 
                + cst.RED + "DATABASE NOT UPDATED !")
            print(cst.YELLOW + "\n There are " + cst.CYAN 
                + f"{len(CATG_RQ.check_category_table())}" 
                + cst.YELLOW + " categories in database.")
        
        else:
            sys.exit(cst.RED + "\n WRONG CHOICE ! Please, choose 'y' or 'n'.\n")

        try:
            while loop:
                print("""\n Choose an option :

     [1]  \033[1;35mUpdate database\033[0;m
     [2]  \033[1;35mDisplay all categories\033[0;m
     [3]  \033[1;38mDisplay all products\033[0;m
     [4]  \033[1;38mAdd products to favorites\033[0;m
     [5]  \033[1;38mDisplay all favorites\033[0;m

     [ui] \033[1;35mGraphical User Interface Mode\033[0;m
     [0c] \033[1;35mClear terminal\033[0;m
     [0x] \033[1;35mExit\033[0;m
        """)
                user_choice = input(cst.CYAN + " >> " + cst.WHITE)
                if user_choice == "ui":
                    ui_app.ui_mode()
                elif user_choice == "0c":
                    logo.logo_connected()
                elif user_choice == "0x":
                    sys.exit(cst.BLUE + "\n Program exit... See you soon ^^\n")
                else:
                    CATG_RQ.category_for_terminal(user_choice)

        except KeyboardInterrupt:
            sys.exit("\n\n" + cst.RED +" Program killed by user..\n")
    
    except KeyboardInterrupt:
        sys.exit("\n\n" + cst.RED +" Program killed by user..\n")


if __name__ == '__main__':
    terminal_mode()