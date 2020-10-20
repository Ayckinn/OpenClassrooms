# -----------------------------------
# -- MODULE FOR DISPLAYING THE LOGO -
# -----------------------------------


import os
from tools import constants as cst


class Logo:

    def __init__(self):
        pass

    def neutral_logo(self):
        os.system('cls')

        print('''                            _________________
        __________________/| \033[1;35mOPEN FOOD FACTS\033[0;m |__________________
      /|                                                        |
     |/|                    ...............                     | 
     |/|  ..................: \033[1;33mDESCRIPTION\033[0;m :...................  |
     |/|  : \033[1;33mShow food categories and products lists from API\033[0;m :  |
     |/|  :                                                  :  |
     |/|  :              ©2020 - Yannick HEUDE               :  |
     |/|  :..................................................:  |
     |/!________________________________________________________!
     |//////////////////////////////////////////////////////////
    ''')

        print(cst.CYAN + "\t\t    OFF VIEWER - TERMINAL MODE\n")

    def logo_connected(self):
        self.neutral_logo()
        print(cst.GREEN + "\t  You are now connected to " + cst.CYAN
              + "Open Food Facts" + cst.GREEN + " database !\n")

    def logo_not_connected(self):
        self.neutral_logo()
        print(cst.RED + " /!\\ DATABASE ACCESS DENIED... "
                        "Please, check your login/password !\n" + cst.RESET)
