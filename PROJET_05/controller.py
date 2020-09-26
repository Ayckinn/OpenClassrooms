# -----------------------------------------
# -- CONTROLLER FOR VIEW MODE MANAGEMENT --
# -----------------------------------------

from database.product_table import Product
from database.category_table import Category


class Controller:

    def __init__(self):
        self.db_product = Product()
        self.db_category = Category()

    # ===== CATEGORY HANDLER =====
    def add_categories_in_db(self):
        return self.db_category.add_categories_in_db()

    def get_number_of_categories_in_db(self):
        return self.db_category.number_of_categories_in_db()

    def get_all_items_in_category_table(self):
        return self.db_category.db_column('*')

    def get_number_of_items_in_id_column(self):
        return self.db_category.db_column('id')

    # ===== PRODUCT HANDLER =====
    def add_product_in_db(self):
        return self.db_product.add_products_in_db()

    def get_number_of_products_in_db(self):
        return self.db_product.number_of_products_in_db()

    def get_all_items_in_product_table(self):
        return self.db_product.db_column('*')

    def get_products_by_category_id(self, cat_id):
        return self.db_product.show_products_by_category_id(cat_id)
