# -------------------------------------
# -- API PRODUCTS REQUEST MANAGEMENT --
# -------------------------------------

import requests


class APIProductManager:
	""" Class for products datas management from API """

	def __init__(self, category_url):
		self.product_api_request = requests.get(category_url + ".json").json()

	def api_product_request_init(self):
		self.get_product_data_from_api = self.product_api_request['products']
		return self.get_product_data_from_api

	def get_data(self, api, key):
		self.product_data = api[key]
		return self.product_data
