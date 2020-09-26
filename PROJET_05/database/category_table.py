# -------------------------------
# -- CATEGORY TABLE MANAGEMENT --
# -------------------------------

from tools import constants as cst
from database.connection import DBConnection
from api.api_category import APICategoryManager


class Category:

    def __init__(self):
        self.db_cnx = DBConnection().db_connect()
        self.cursor = self.db_cnx.cursor()

        self.api_category = APICategoryManager()

    def table_keys(self, category_id, name, url):
        self.id = category_id
        self.name = name
        self.url = url

        self.get_value_keys = (category_id, name, url)
        return self.get_value_keys

    def db_column(self, column):
        self.cursor.execute(f"SELECT {column} FROM {cst.DB_NAME}.{cst.CATEGORY_TABLE}")
        self.query = self.cursor.fetchall()

        return self.query

    def add_categories_in_db(self):
        self.category_index = 0
        for category in range(100):
            self.cursor.execute(f"INSERT INTO {cst.DB_NAME}.{cst.CATEGORY_TABLE}"
                                f"(id, name, url) VALUES (NULL, %s, %s)",
                                (self.api_category.get_category_name(self.category_index),
                                 self.api_category.get_category_url(self.category_index)))
            self.category_index += 1
        self.db_cnx.commit()

    def number_of_categories_in_db(self):
        print(cst.YELLOW + "\n Categories in database : " + cst.CYAN
              + f"{len(self.db_column('id'))}")

    def get_category_list_from_db(self):
        self.category_db_list = []

        for row in self.db_column('*'):
            self.add_values = self.table_keys(
                row[0],  # -- ID --
                row[1],  # -- Name --
                row[2])  # -- URL --
            self.category_db_list.append(self.add_values)

        return self.category_db_list
