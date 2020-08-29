# -*- coding: UTF-8 -*-

# ===========================================================
# =            OPEN FOOD FACTS DATABASE HANDLING            =
# =               OPENCLASSROOMS - PROJECT 05               =
# =                                                         =
# =    Use publics datas from OpenFood Facts API            =
# =    Display categories and products in TERMINAL VERSION  =
# = =========================================================


import sys
import ui_app

from db_requests import categories
from tools import constants as cst
from logo import logo


def terminal_mode():
    cat_rq = categories.Category()
    loop = True
    
    try:
        print(cst.CYAN + "\t\t    OFF VIEWER - TERMINAL MODE\n\n")
        user_response = input(" Do you want to update database (y/n) : ").lower()
        if user_response == 'y':
            cat_rq.create_category_table()
            print(cst.MAGENTA + "\n DATABASE STATUS => " + cst.GREEN + "DATABASE UPDATED SUCCESSFULLY...")
        elif user_response == 'n':
            print(cst.MAGENTA + "\n DATABASE STATUS => " + cst.RED + "DATABASE NOT UPDATED !")
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

     [ui] \033[1;35mUI Mode\033[0;m
     [0c] \033[1;35mClear terminal\033[0;m
     [0x] \033[1;35mExit\033[0;m
        """)
                user_choice = input(cst.CYAN + " >> " + cst.WHITE)
                if user_choice == "ui":
                    ui_app.ui_mode()
                elif user_choice == "0c":
                    logo.logo()
                    print(cst.CYAN + "\t\t    OFF VIEWER - TERMINAL MODE\n")
                elif user_choice == "0x":
                    sys.exit(cst.BLUE + "\n Program exit... See you soon ^^\n")
                else:
                    cat_rq.category_for_terminal(user_choice)

        except KeyboardInterrupt:
            sys.exit("\n\n" + cst.RED +" Program killed by user..\n")
    
    except KeyboardInterrupt:
        sys.exit("\n\n" + cst.RED +" Program killed by user..\n")


if __name__ == '__main__':
    terminal_mode()