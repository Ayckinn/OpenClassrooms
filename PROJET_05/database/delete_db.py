from tools import constants as cst
from mysql.connector import Error, ProgrammingError
from database.db_provider import DBProvider


class DeleteDB:

    def __init__(self):
        self.db_cnx = DBProvider().get_db()
        self.cursor = self.db_cnx.cursor()

    def delete_table(self, table):
        self.cursor.execute(f"DELETE FROM {table} WHERE id > 0")
        self.db_cnx.commit()

    def delete_database(self):
        print()
        self.delete_table(cst.CATEGORY_TABLE)
        self.delete_table(cst.PRODUCT_TABLE)
        self.delete_table(cst.FAVORITE_TABLE)
        
        self.db_cnx.close()
