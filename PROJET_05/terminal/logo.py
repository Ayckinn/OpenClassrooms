# -----------------------------------
# -- MODULE FOR DISPLAYING THE LOGO -
# -----------------------------------


import os
from tools import constants as cst


def logo():
    os.system('cls')

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

    print(cst.CYAN + "\t\t    OFF VIEWER - TERMINAL MODE\n\n")

# //////////////////////////////////////////////////////////////////////////////////////////

def logo_connected():
    os.system('cls')

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

    print(cst.CYAN + "\t\t    OFF VIEWER - TERMINAL MODE\n\n")
    print(cst.GREEN + "      You are now connected to " + cst.CYAN + "Open Food Facts" 
    	+ cst.GREEN + " database !")
    print(cst.RED + "\t /!\\ BE CAREFULL WHEN YOU ARE HANDLING DATAS !!\n")

# //////////////////////////////////////////////////////////////////////////////////////////

def logo_not_connected():
    os.system('cls')

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

    print(cst.CYAN + "\t\t    OFF VIEWER - TERMINAL MODE\n\n")
    print(cst.RED + " /!\\ DATABASE ACCESS DENIED... "
    	"Please retry later or check your login/password !\n" + cst.RESET)