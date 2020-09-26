# ------------------------------
# -- PRODUCT TABLE MANAGEMENT --
# ------------------------------

from tools import constants as cst
from database.category_table import Category
from database.connection import DBConnection
from api.api_product import APIProductManager


class Product:

    def __init__(self):
        self.db_cnx = DBConnection().db_connect()
        self.cursor = self.db_cnx.cursor()
        self.category_list = Category().get_category_list_from_db()

    def db_column(self, column):
        self.cursor.execute(f"SELECT {column} FROM {cst.DB_NAME}.{cst.PRODUCT_TABLE}")
        self.query = self.cursor.fetchall()

        return self.query

    def add_products_in_db(self):
        self.category_index = 0

        for category in self.category_list:
            self.category_id = self.category_list[self.category_index][0]
            self.category_name = self.category_list[self.category_index][1]
            self.category_url = self.category_list[self.category_index][2]
            self.category_index += 1

            self.api_product = APIProductManager(self.category_url)
            self.product_index = 0

            for product in self.api_product.api_product_request_init():
                try:
                    self.json_product_data = self.api_product.api_product_request_init()[self.product_index]
                    self.cursor.execute(f"INSERT INTO {cst.DB_NAME}.{cst.PRODUCT_TABLE}"
                                        "(id, name, brand, nutriscore, url, category_id)"
                                        "VALUES(NULL, %s, %s, %s, %s, %s)",
                                        (self.api_product.get_data(self.json_product_data, 'product_name'),
                                         self.api_product.get_data(self.json_product_data, 'brands'),
                                         self.api_product.get_data(self.json_product_data, 'nutriscore_grade'),
                                         self.api_product.get_data(self.json_product_data, 'url'),
                                         self.category_id))

                    self.product_index += 1
                except KeyError:
                    pass

        self.db_cnx.commit()

    def number_of_products_in_db(self):
        print(cst.YELLOW + " Products in database   : " + cst.CYAN
              + f"{len(self.db_column('id'))}")

    def show_products_by_category_id(self, cat_id):
        self.cursor.execute(f"SELECT * FROM {cst.DB_NAME}.{cst.PRODUCT_TABLE}\
                            WHERE category_id = {cat_id}")
        self.show_products = self.cursor.fetchall()

        return self.show_products