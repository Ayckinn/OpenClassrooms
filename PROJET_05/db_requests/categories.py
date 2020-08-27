import requests
from db_access import db_access
from logo import logo


def create_category_table():
    db_name = "openfoodfact"
    table_name = "Categories"

    db_access.db_connect()
    db_cnx = db_access.db_connect()
    cursor = db_cnx.cursor()
    logo.logo()

    api_link = "https://fr.openfoodfacts.org/categories.json"
    json_data_rq = requests.get(api_link).json()

    index = 0
    for _ in json_data_rq:
        cursor.execute(f"INSERT INTO {db_name}.{table_name} (id, name, url, nb_products)"
                       "VALUES (NULL, %s, %s, %s)",
                       (json_data_rq['tags'][index]['name'],
                        json_data_rq['tags'][index]['url'],
                        json_data_rq['tags'][index]['products']))
        index += 1

    db_cnx.commit()