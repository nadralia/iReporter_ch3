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
            self.con.autocommit = True
            self.dict_cursor = self.con.cursor(cursor_factory=extra.RealDictCursor)
            self.create_tables()
        except Exception as ex:
            pprint("Database connection error: "+str(ex))

    def create_tables(self):
        create_tables = (
            """
             CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY NOT NULL,
                    firstname VARCHAR (40) NOT NULL,
                    lastname VARCHAR (40) NOT NULL,
                    othernames VARCHAR(40),
                    email VARCHAR(60) UNIQUE NOT NULL,
                    username VARCHAR (40) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    phonenumber VARCHAR(14) UNIQUE NOT NULL,
                    gender VARCHAR(14) NOT NULL,
                    is_admin VARCHAR(14) DEFAULT 'False',
                    registered TIMESTAMP WITH TIME ZONE DEFAULT now(),
                    updatedOn TIMESTAMP WITH TIME ZONE DEFAULT now()
             )
            """,

            """
			CREATE TABLE IF NOT EXISTS incidents (
                    incident_id SERIAL PRIMARY KEY NOT NULL,
                    incident_unique VARCHAR(100) NOT NULL,
                    createdBy INTEGER REFERENCES users(user_id),
                    incident_type VARCHAR(15) NOT NULL,
                    status VARCHAR(50) DEFAULT 'drafted', 
                    latitude VARCHAR(25) NOT NULL,
                    longitude VARCHAR(25) NOT NULL,
                    images VARCHAR(100),
                    videos VARCHAR(100),
                    comment VARCHAR(255) NOT NULL,
                    createdOn TIMESTAMP WITH TIME ZONE DEFAULT now(),
                    updatedOn TIMESTAMP WITH TIME ZONE DEFAULT now()
			)
			"""
        )
        for table in create_tables:
            self.dict_cursor.execute(table)
   

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


