# -----------------------------------
# -- MODULE FOR DISPLAYING THE LOGO -
# -----------------------------------

import os

from tools import constants as cst


def logo():
    os.system('cls')

    print(cst.GREEN + "\n You are now connected to " + cst.CYAN
          + "OpenFoodFact" + cst.GREEN + " database !")

    print(cst.RED + "\n  /!\\ BE CAREFULL WHEN YOU ARE HANDLING DATAS !!\n")

    print('''                        _________________
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
