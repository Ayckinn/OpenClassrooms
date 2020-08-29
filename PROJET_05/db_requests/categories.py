# ---------------------------------
# -- CATEGORIES TABLE MANAGEMENT --
# ---------------------------------


import requests
import sys
import time

from db_access import db_access
from logo import logo
from tools import constants as cst


sql_cnx = db_access.DBcnx()


class Category:
    """
    Class used for display categories and management 
    """


    def __init__(self):
        self.db_cnx = sql_cnx.db_connect()
        self.cursor = self.db_cnx.cursor()


    def create_category_table(self):
        self.api_link = "https://fr.openfoodfacts.org/categories.json"
        self.json_data_rq = requests.get(self.api_link).json()

        self.index = 0
        for _ in self.json_data_rq['tags']:
            self.cursor.execute(f"INSERT INTO {cst.DB_NAME}.{cst.CATG_TABLE}"
                                f"(id, name, url, nb_products) VALUES (NULL, %s, %s, %s)",
                                (self.json_data_rq['tags'][self.index]['name'],
                                 self.json_data_rq['tags'][self.index]['url'],
                                 self.json_data_rq['tags'][self.index]['products']))
            self.index += 1

        self.db_cnx.commit()


    def check_category_table(self):
        self.cursor.execute(f"SELECT id FROM {cst.DB_NAME}.{cst.CATG_TABLE}")
        self.catg_id = self.cursor.fetchall()

        return self.catg_id


    def category_for_terminal(self, choice): 
        if choice == "1":
            self.create_category_table()
            print(cst.MAGENTA + "\n DATABASE STATUS => " + cst.GREEN + "DATABASE UPDATED SUCCESSFULLY...\n")

        elif choice == "2":
            if len(self.check_category_table()) == 0:  # -- If table is empty
                    print(cst.MAGENTA + "\n Categories table is empty...")
                    time.sleep(3)
                    logo.logo()
            else:
                self.display_category_list()

        else:
            print(cst.RED + "\n WRONG CHOICE ! Please, select with 'y' or 'n'.\n")
            print("")


    def display_category_list(self):
        self.cursor.execute(f"SELECT * FROM {cst.DB_NAME}.{cst.CATG_TABLE}")
        self.categories = self.cursor.fetchall()

        for catg in self.categories:
            print(cst.YELLOW + str(catg))
        print("")