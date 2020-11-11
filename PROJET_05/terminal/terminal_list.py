# -----------------------------------------
# -- MODULE FOR TERMINAL LIST MANAGEMENT --
# -----------------------------------------

from terminal.logo import Logo


class ListOptions:

    def __init__(self):
        pass

    def print_list(self):
        print("""\n Choose an option :

   [1] \033[1;35mAdd categories in database\033[0;m
   [2] \033[1;35mDisplay all categories\033[0;m
   [3] \033[1;35mAdd products in database\033[0;m
   [4] \033[1;35mDisplay all products\033[0;m
   [5] \033[1;35mChoose a category to display associated products\033[0;m
   [6] \033[1;35mAdd product to favorites\033[0;m
   [7] \033[1;35mDisplay all favorites\033[0;m
   [8] \033[1;35mDelete database\033[0;m

   [i] \033[1;35mGraphical User Interface Mode\033[0;m
   [c] \033[1;35mClear terminal\033[0;m
   [x] \033[1;35mExit\033[0;m
""")
