from api.database.db_connection import DatabaseConnection

class DBFunctions:
    def __init__(self):
        self.connect = DatabaseConnection()
        self.cursor = self.connect.dict_cursor

    def add_new_user(self,firstname, lastname, othernames,email, username, 
        password,phonenumber,gender,registered,is_admin):
        """ insert a new user in table users"""
        query = (
            """INSERT INTO users (firstname, lastname,othernames, email,username, 
            password,phonenumber,gender,registered,is_admin) 
            VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}','{}','{}'
            )""".format(firstname,lastname,othernames,email, username,password,
            phonenumber,gender,registered,is_admin))

        self.cursor.execute(query)

    def check_username(self,username):
        """check if username exists."""
        query = ("""SELECT * FROM users where username = '{}'""".format(username))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        if user:
            return user
        return False  

    def user_login(self, username, password):
        """login a user"""
        query = ("""SELECT * from users where username = '{}' and password='{}'""".format(username, password))
        self.cursor.execute(query)
        user =self.cursor.fetchone()
        return user  

    def fetch_a_user(self, username):
        """fetch a user details"""
        self.cursor.execute("SELECT * FROM users WHERE username = '{}'" .format(username))
        row = self.cursor.fetchone()
        return row