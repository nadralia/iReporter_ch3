from api.database.db_connection import DatabaseConnection

class UserModel:
    def __init__(self, **kwargs):
        """ stores user details """
        self.firstname = kwargs.get('firstname')
        self.lastname = kwargs.get('lastname')
        self.othernames = kwargs.get('othernames')
        self.email = kwargs.get('email')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.phonenumber = kwargs.get('phonenumber')
        self.gender = kwargs.get('gender')
        self.is_admin = kwargs.get('is_admin')
        self.connect = DatabaseConnection()
        self.cursor = self.connect.dict_cursor

    def add_new_user(self,firstname, lastname, othernames,email, username, 
        password,phonenumber,gender,is_admin):
        """ insert a new user in table users"""
        query = (
            """INSERT INTO users (firstname, lastname,othernames, email,username, 
            password,phonenumber,gender,is_admin) 
            VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}','{}'
            )""".format(firstname,lastname,othernames,email, username,password,
            phonenumber,gender,is_admin))

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
        self.cursor.execute("SELECT user_id, username, email,is_admin FROM users WHERE username = '{}'" .format(username))
        row = self.cursor.fetchone()
        return row