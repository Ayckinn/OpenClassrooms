# -------------------------------
# -- PRODUCTS DATAS MANAGEMENT --
# -------------------------------

import requests

from db_access import db_access
from db_requests import categories
from tools import constants as cst

category_request = categories.Category()
category_list = category_request.create_category_list_from_db()
sql_connection = db_access.DBConnection()


class Products:

	def __init__(self):
		self.db_connection = sql_connection.db_connect()
		self.cursor = self.db_connection.cursor()


	def db_column(self, column):
		self.cursor.execute(f"SELECT {column} FROM {cst.DB_NAME}.{cst.PRODUCTS_TABLE}")
		self.query = self.cursor.fetchall()

		return self.query


	def add_products_in_db(self):
		# -- Block for management categories list --
		self.category_index = 0
		for category in category_list:
			self.category_id = category_list[self.category_index][0]
			self.category_name = category_list[self.category_index][1]
			self.category_url = category_list[self.category_index][2]		
			self.category_index += 1

			# -- Block for management to add products in database --
			self.product_index = 0
			self.product_json_request = requests.get(self.category_url + ".json").json()
			self.get_product_data_in_json = self.product_json_request['products']
			
			for product in self.get_product_data_in_json:
				try:
					self.api_product_data = self.get_product_data_in_json[self.product_index]

					self.cursor.execute(f"INSERT INTO {cst.DB_NAME}.{cst.PRODUCTS_TABLE}"
										"(id, name, brand, nutriscore, url, category_id)"
										"VALUES(NULL, %s, %s, %s, %s, %s)",
										(self.api_product_data['product_name'],
									     self.api_product_data['brands'],
									     self.api_product_data['nutriscore_grade'],
									     self.api_product_data['url'],
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
