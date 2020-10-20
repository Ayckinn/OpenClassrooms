# -----------------------------------------
# -- CONTROLLER FOR VIEW MODE MANAGEMENT --
# -----------------------------------------

from database.delete_db import DeleteDB
from database.product_table import Product
from database.category_table import Category
from database.favorite_table import Favorite


class Controller:

    def __init__(self):
        self.del_db = DeleteDB()
        self.db_product = Product()
        self.db_category = Category()
        self.db_favorite = Favorite()

    def delete_database(self):
        return self.del_db.delete_database()

    # ===== CATEGORY HANDLER =====
    def add_categories_in_db(self):
        return self.db_category.add_categories_in_db()

    def get_number_of_categories_in_db(self):
        return self.db_category.number_of_categories_in_db()

    def get_items_in_category_table(self, key):
        return self.db_category.db_column(key)

    # ===== PRODUCT HANDLER =====
    def add_product_in_db(self):
        return self.db_product.add_products_in_db()

    def get_number_of_products_in_db(self):
        return self.db_product.number_of_products_in_db()

    def get_items_in_product_table(self, key):
        return self.db_product.db_column(key)

    def get_products_by_category_id(self, cat_id):
        return self.db_product.show_products_by_category_id(cat_id)

    # ===== FAVORITE HANDLER =====
    def add_product_in_favorite(self, user_choice):
        return self.db_favorite.add_product_in_favorite(user_choice)
        
    def get_product_by_id(self, prod_id):
        return self.db_product.show_product_by_id(prod_id)

    def get_items_in_favorite_table(self, key):
        return self.db_favorite.db_column(key)

    def get_number_of_favorite_in_db(self):
        return self.db_favorite.number_of_favorites_in_db()

    # ===== FOR UI MODE =====
    def display_number_of_categories_in_db(self):
        return str(len(self.get_items_in_category_table('id')))

    def display_number_of_products_in_db(self):
        return str(len(self.get_items_in_product_table('id')))

    def display_number_of_favorites_in_db(self):
        return str(len(self.get_items_in_favorite_table('id')))
