from api.models.user import UserModel

class UserController:
    def __init__(self):
        self.user_m = UserModel()

    def create_new_user(self,email, username, password,is_admin):
        """ create a new user and insert in the users table"""
        new_user = UserModel(email=email,username=username, password=password,is_admin=is_admin)
        
        self.user_m.add_new_user(email=new_user.email,username=new_user.username,password=new_user.password,
                   is_admin=new_user.is_admin)
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