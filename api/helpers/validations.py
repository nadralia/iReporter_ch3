import re

class Validation:
   
    def validate_name(self, name):
        """
        validates the name input
        """
        if name.strip() == "" or len(name.strip()) < 3:
            return "Enter name with more than 2 characters please"
        if len(name.strip()) > 25:
            return  "Enter name with 25 characters or less"
        if not bool(re.fullmatch('^[A-Za-z ]*$', name)):
            return "Invalid characters not allowed"
        return True

    def validate_password(self, password):
        """check the validity of password input by users"""
        if (len(password)<6 or len(password)>12): 
            return "Minimum length of password: 6 and  Maximum length of password: 12"
        elif not re.search("[a-z]",password):
            return "Password must have atleast 1 lowercase character [a-z]"
        elif not re.search("[A-Z]",password):
            return "Password must have atleast 1 uppercase character [A-Z]"
        elif not re.search("[0-9]",password):
            return "Password must have atleast 1 number between [0-9]"
        elif not re.search("[$#@]",password):
            return "Password must have atleast 1 character from [$#@]"
        else:
            return "Valid Password"

    def validate_user(self, username,email,gender):
        """ Validates user fields"""
        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",email):
            return "Invalid email format"
        if not re.match(r"([a-zA-Z0-9]*$)", username):
            return "Only alphanumerics allowed in user name"
        if gender != 'Male' and gender != 'Female':
            return "Genger must be either Male or Female"
        else:
            return "is_valid"
            
    def validate_login(self, username, password):
        """
        validates the user login input
        """
        try:
            if username == "" or password == "":
                return "Input username or password"
            else:
                return "Credentials valid"
        except KeyError:
            return "Invalid fields"
