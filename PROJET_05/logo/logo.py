import colorama
import os
from colorama import Fore

colorama.init()

def logo():
    os.system('cls')
    print(Fore.GREEN + "\n You are now connected to " + Fore.CYAN
          + "OpenFoodFact" + Fore.GREEN + " database !" + Fore.RESET)
    print(Fore.RED + "\n  /!\\ BE CAREFULL WHEN YOU ARE HANDLING DATAS !!\n" + Fore.RESET)
    print('''                        _________________
    __________________/| \033[1;35mOPEN FOOD FACTS\033[0;m |__________________
  /|                                                        |
 |/|                    ...............                     | 
 |/|  ..................: \033[1;33mDESCRIPTION\033[0;m :...................  |
 |/|  : \033[1;33mShow food categories and products lists from API\033[0;m :  |
 |/|  :..................................................:  |
 |/!________________________________________________________!
 |//////////////////////////////////////////////////////////
''')