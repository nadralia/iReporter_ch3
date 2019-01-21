from api.database.db_connection import DatabaseConnection

class DBFunctions:
    def __init__(self):
        self.connect = DatabaseConnection()
        self.cursor = self.connect.dict_cursor

    def add_new_user(self,firstname, lastname,email, username, 
        password,phonenumber,gender,registered,is_admin):
        """ insert a new user in table users"""
        query = (
            """INSERT INTO users (firstname, lastname,email,username, 
            password,phonenumber,gender,registered,is_admin) 
            VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}','{}'
            )""".format(firstname,lastname,email, username,password,
            phonenumber,gender,registered,is_admin))

        self.cursor.execute(query)