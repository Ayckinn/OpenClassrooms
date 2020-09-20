# --------------------------------------
# -- PRODUCTS JSON REQUEST MANAGEMENT --
# --------------------------------------

import requests

from tools import constants as cst
from db_requests import db_categories


class JSONProducts:
	""" Class for prodcuts json datas management """

	def __init__(self, category_url):
		self.product_json_request = requests.get(category_url + ".json").json()


	def json_product_request_init(self):
		self.get_product_data_from_json = self.product_json_request['products']
		return self.get_product_data_from_json


	def get_data(self, api, key):
		self.product_data = api[key]
		return self.product_data
