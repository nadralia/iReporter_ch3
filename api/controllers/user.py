from api.database.db_functions import DBFunctions
from api.models.user import UserModel

class UserController:
    def __init__(self):
        self.dbfunctions = DBFunctions()

    def create_new_user(self,firstname, lastname,email, username, 
        password,phonenumber,gender,registered,is_admin):
        """ create a new user"""
        new_user = UserModel(firstname=firstname, lastname=lastname,email=email,
                        username=username, password=password,phonenumber=phonenumber,
                        gender=gender,registered=registered,is_admin=is_admin)

        self.dbfunctions.add_new_user(firstname=new_user.firstname, lastname=new_user.lastname,
                    email=new_user.email,username=new_user.username, password=new_user.password, 
                    phonenumber=new_user.phonenumber,gender=new_user.gender,
                            registered=new_user.registered,is_admin=new_user.is_admin)
        return True