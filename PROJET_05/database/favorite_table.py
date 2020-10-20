# -------------------------------
# -- FAVORITE TABLE MANAGEMENT --
# -------------------------------

from datetime import datetime

from tools import constants as cst
from database.product_table import Product
from mysql.connector import IntegrityError
from database.db_provider import DBProvider


class Favorite:

    def __init__(self):
        self.db_cnx = DBProvider().get_db()
        self.cursor = self.db_cnx.cursor()

    def db_column(self, column):
        self.cursor.execute(f"SELECT {column} FROM {cst.DB_NAME}.{cst.FAVORITE_TABLE}")
        self.query = self.cursor.fetchall()

        return self.query

    def add_product_in_favorite(self, product):
        self.date_now = datetime.now()

        try:
            self.cursor.execute(f"INSERT INTO {cst.DB_NAME}.{cst.FAVORITE_TABLE}"
                                "(id, product_name,\
                                  product_brand,\
                                  product_nutriscore,\
                                  product_url,\
                                  product_id,\
                                  add_date)"
                                "VALUES(NULL, %s, %s, %s, %s, %s, %s)",
                                (product[1],
                                 product[2],
                                 product[3],
                                 product[4],
                                 product[0],
                                 self.date_now))
        except IntegrityError:
            print(cst.ALREADY_IN_FAVORITES_MSG)

        self.db_cnx.commit()

    def number_of_favorites_in_db(self):
        print(cst.YELLOW + " Favorites in database  : " + cst.CYAN
              + f"{len(self.db_column('id'))}")
        print()
