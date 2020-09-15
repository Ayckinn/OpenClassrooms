# ---------------------------------
# -- CATEGORIES TABLE MANAGEMENT --
# ---------------------------------

import sys
import requests

from term import logo
from db_access import db_access
from tools import constants as cst

sql_connection = db_access.DBConnection()


class Category:
    """
    Class used to display categories and management 
    """

    def __init__(self):
        self.db_connection = sql_connection.db_connect()
        self.cursor = self.db_connection.cursor()


    def category_db_keys(self, category_id, name, url):
        self.id = category_id
        self.name = name
        self.url = url

        self.get_value_keys = (category_id, name, url)

        return self.get_value_keys


    def db_column(self, column):
        self.cursor.execute(f"SELECT {column} FROM {cst.DB_NAME}.{cst.CATEGORIES_TABLE}")
        self.query = self.cursor.fetchall()

        return self.query

        
    def add_categories_in_db(self):
        self.json_data_request = requests.get(cst.CATEGORIES_JSON_URL).json()

        self.category_index = 0
        for categorie in range(100):
            self.cursor.execute(f"INSERT INTO {cst.DB_NAME}.{cst.CATEGORIES_TABLE}"
                                f"(id, name, url) VALUES (NULL, %s, %s)",
                                (self.json_data_request['tags'][self.category_index]['name'],
                                 self.json_data_request['tags'][self.category_index]['url']))
            self.category_index += 1

        self.db_connection.commit()


    def show_categories_number_in_db(self):
        print(cst.YELLOW + "\n Categories in database : " + cst.CYAN
              + f"{len(self.db_column('id'))}")


    def create_category_list_from_db(self):
        self.category_db_list = []

        for row in self.db_column('*'):
            self.add_values = self.category_db_keys(
                row[0],  # -- ID --
                row[1],  # -- Name --
                row[2])  # -- URL --
            self.category_db_list.append(self.add_values)

        return self.category_db_list
