# -------------------------------
# -- PRODUCTS DATAS MANAGEMENT --
# -------------------------------

import requests

from db_access import db_access
from tools import constants as cst
from db_requests import db_categories
from api_request import json_products

sql_connection = db_access.DBConnection()
category_request = db_categories.Category()
category_list = category_request.create_category_list_from_db()


class Products:
	"""
    Class used to display products and management 
    """

	def __init__(self):
		self.db_connection = sql_connection.db_connect()
		self.cursor = self.db_connection.cursor()


	def db_column(self, column):
		self.cursor.execute(f"SELECT {column} FROM {cst.DB_NAME}.{cst.PRODUCTS_TABLE}")
		self.query = self.cursor.fetchall()

		return self.query


	def add_products_in_db(self):
		# -- Block for management categories list from DB --
		self.category_index = 0

		for category in category_list:
			self.category_id = category_list[self.category_index][0]
			self.category_name = category_list[self.category_index][1]
			self.category_url = category_list[self.category_index][2]		
			self.category_index += 1

			# -- Block for management to add products in database --
			self.api_product = json_products.JSONProducts(self.category_url)
			self.product_index = 0
			
			for product in self.api_product.json_product_request_init():
				try:
					self.json_product_data = self.api_product.json_product_request_init()[self.product_index]
					self.cursor.execute(f"INSERT INTO {cst.DB_NAME}.{cst.PRODUCTS_TABLE}"
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

		self.db_connection.commit()


	def show_products_number_in_db(self):
		print(cst.YELLOW + " Products in database   : " + cst.CYAN
			+ f"{len(self.db_column('id'))}")


	def display_products_for_a_category(self, choice):
		self.cursor.execute(f"SELECT * FROM {cst.DB_NAME}.{cst.PRODUCTS_TABLE}\
							WHERE Category_id = {choice}")
		self.user_response = self.cursor.fetchall()

		return self.user_response
