from database.connection import DBConnection


class DBProvider:

	def __init__(self):
		self.db = DBConnection()

	def get_db(self):
		if not self.db.is_connected:
			self.db.connect()

		return self.db.dbconnect
