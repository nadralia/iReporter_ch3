import psycopg2
import psycopg2.extras as extra
from pprint import pprint
from codecs import open
import os


class DatabaseConnection:
    def __init__(self):
        """Make a connection to the database"""
        try:
            if os.environ["APP_SETTINGS"] == "DEVELOPMENT":
                self.con = psycopg2.connect(
                    database=os.environ["DATABASE_NAME"], user=os.environ["DATABASE_USER"], 
                    password=os.environ["DATABASE_PASSWORD"], host=os.environ["DATABASE_HOST"], 
                    port=os.environ["DATABASE_PORT"])
            else:
                self.con = psycopg2.connect(
                    database=os.environ["DATABASE_NAME"], user=os.environ["DATABASE_USER"], 
                    password=os.environ["DATABASE_PASSWORD"], host=os.environ["DATABASE_HOST"], 
                    port=os.environ["DATABASE_PORT"])
            self.con.autocommit = True
            self.dict_cursor = self.con.cursor(cursor_factory=extra.RealDictCursor)
        except Exception as ex:
            pprint("Database connection error: "+str(ex))

    def create_tables(self):
        create_users_table = open(
            'api/database/create_users.sql', mode='r', encoding='utf-8-sig').read()
        create_incidents_table = open(
            'api/database/create_incidents.sql', mode='r', encoding='utf-8-sig').read()
        queries = (create_users_table,create_incidents_table)

        for query in queries:
            self.dict_cursor.execute(query)
   

    def delete_tables(self):
        delete_queries = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,
            """
			DROP TABLE IF EXISTS incidents CASCADE
			""")
        for query in delete_queries:
            self.dict_cursor.execute(query)


