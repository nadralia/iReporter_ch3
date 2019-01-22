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
        self.registered = kwargs.get('registered')
        self.is_admin = False