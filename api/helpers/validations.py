import re

class Validation:
    
    def check_if_input_is_number(self, input_value):
        """function to checks if input value is a number"""
        if isinstance(input_value, int) or isinstance(input_value, float):
            return True
        return False

    def check_if_input_value_is_string(self, input_value):
        """function to checks if input value  is a string"""
        if (
            isinstance(input_value, str)
            and not str(input_value).isspace()
            and not input_value.isnumeric()
        ):
            return True
        return False

    def check_if_input_contains_space(self, input_value):
        """function to checks if input value contains space"""
        if " " in input_value or len(str(input_value).split(" ")) > 1:
            return True
        return False

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
            return True

    def validate_user_details(self, username,email,gender):
        """ Validates user fields"""
        if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)",email):
            return "Invalid email format"
        if not re.match(r"([a-zA-Z0-9]*$)", username):
            return "Only alphanumerics allowed in user name"
        if gender != 'Male' and gender != 'Female':
            return "Gender must be either Male or Female"
        if not username or username == " ":
            return "usename is missing"
            
    def validate_login(self, username, password):
        """
        validates the user login input
        """
        if username == "" or password == "":
            return "Input username or password"

    def validate_incident(self, incident_type,comment):
        """ add incident validation."""
        if comment == "":
            return "Comment of the incident is missing"
        if incident_type == "":
           return "Type of incident is missing"
        elif str(incident_type).lower() not in (
            "red-flag",
            "intervention"
        ):
            return "Type of incident must be either Red-flag or Intervention"

    
    def validate_location(self, latitude, longitude):
        """ validate latitude and longitude """
        if not self.check_if_input_is_number(latitude) or not self.check_if_input_is_number(longitude):
            return "location coordinates must be a number"
    
    def validate_status(self, status):
        if not status or not isinstance(status, str):
            return "Status is missing"
        elif str(status).lower() not in (
            "drafted",
            "resolved",
            "under investigation",
            "rejected"
        ):
            return "Status must be one of these drafted,resolved,under investigation,rejected"
    
    def validate_input_type(self, input):
        """check if the input values is an integer"""
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an interger"

