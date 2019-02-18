from api.models.user import UserModel

class UserController:
    def __init__(self):
        self.user_m = UserModel()

    def create_new_user(self,firstname, lastname,othernames, email, username, 
        password,phonenumber,gender,is_admin,profile_pic):
        """ create a new user and insert in the users table"""
        new_user = UserModel(firstname=firstname, lastname=lastname, othernames=othernames, email=email,
                        username=username, password=password,phonenumber=phonenumber,
                        gender=gender,is_admin=is_admin,profile_pic=profile_pic)

        self.user_m.add_new_user(firstname=new_user.firstname, lastname=new_user.lastname,
                   othernames=new_user.othernames, email=new_user.email,username=new_user.username, 
                   password=new_user.password, phonenumber=new_user.phonenumber,gender=new_user.gender,
                   is_admin=new_user.is_admin,profile_pic=new_user.profile_pic)
        return True

    def check_if_username_exists(self, username):
        """check if the supplied username already exists."""
        username_exists = self.user_m.check_username(username=username)
        if username_exists:
            return username_exists
        return False

    def get_user(self, username):
        """ get a user """
        login = self.user_m.fetch_a_user(username=username)
        if login:
            return login
        return False

    def fetch_all_users(self):
        """fetch all available users"""
        available_users = self.user_m.get_all_users()
        return available_users 