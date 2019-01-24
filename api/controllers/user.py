from api.database.db_functions import DBFunctions
from api.models.user import UserModel

class UserController:
    def __init__(self):
        self.dbfunctions = DBFunctions()

    def create_new_user(self,firstname, lastname,othernames, email, username, 
        password,phonenumber,gender,is_admin):
        """ create a new user and insert in the users table"""
        new_user = UserModel(firstname=firstname, lastname=lastname, othernames=othernames, email=email,
                        username=username, password=password,phonenumber=phonenumber,
                        gender=gender,is_admin=is_admin)

        self.dbfunctions.add_new_user(firstname=new_user.firstname, lastname=new_user.lastname,
                   othernames=new_user.othernames, email=new_user.email,username=new_user.username, 
                   password=new_user.password, phonenumber=new_user.phonenumber,gender=new_user.gender,
                            is_admin=new_user.is_admin)
        return True

    def check_if_username_exists(self, username):
        """check if the supplied username already exists."""
        username_exists = self.dbfunctions.check_username(username=username)
        if username_exists:
            return username_exists
        return False

    def get_user(self, username):
        """ get a user """
        login = self.dbfunctions.fetch_a_user(username=username)
        if login:
            return login
        return False