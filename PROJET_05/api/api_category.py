# ---------------------------------------
# -- API CATEGORIES REQUEST MANAGEMENT --
# ---------------------------------------

import requests
from tools import constants as cst


class APICategoryManager:
	""" Class for categories datas management from API """

	def __init__(self):
		self.json_data_request = requests.get(cst.CATEGORIES_JSON_URL).json()

	def get_category_name(self, index):
		self.category_name = self.json_data_request['tags'][index]['name']
		return self.category_name

	def get_category_url(self, index):
		self.category_url = self.json_data_request['tags'][index]['url']
		return self.category_url
