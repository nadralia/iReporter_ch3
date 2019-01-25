import unittest
from api.helpers.validations import Validation
from api import app


class TestValidation(unittest.TestCase):
    """ Tests Reflag and user validations """

    def setUp(self):
        """Sets up the validation class """
        self.validation = Validation()

    def test_validate_name(self):
        """Tests to ensure the correct data definition passes"""
        data = "Adralia"
        self.assertEqual(self.validation.validate_name(data), 
         True)
    
    def test_validate_empty_name(self):
        """Tests to ensure the correct data definition passes"""
        data = ""
        self.assertEqual(self.validation.validate_name(data), 
        "Enter name with more than 2 characters please")

    def test_validate_name_less_25(self):
        """Tests to ensure the correct data definition passes"""
        data = "Enternamewithcharactersorless"
        self.assertEqual(self.validation.validate_name(data), 
        "Enter name with 25 characters or less")

    def test_validate_name_invalid_chars(self):
        """Tests to ensure the correct data definition passes"""
        data = "nadr$%rt"
        self.assertEqual(self.validation.validate_name(data), 
        "Invalid characters not allowed")

    def test_if_its_a_validate_password(self):
        password = 'Nadra2922@'
        result = self.validation.validate_password(password)
        self.assertEqual(result, True)
 
    def test_minimum_length_of_password(self):
        password = 'Nadra'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Minimum length of password: 6 and  Maximum length of password: 12")

    def test_maximum_length_of_password(self):
        password = 'Nadra2922@as2#'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Minimum length of password: 6 and  Maximum length of password: 12")

    def test_lowercase_character(self):
        password = 'NADRA2922#'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Password must have atleast 1 lowercase character [a-z]")

    def test_uppercase_character(self):
        password = 'nadra2922#'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Password must have atleast 1 uppercase character [A-Z]")
    
    def test_number_character(self):
        password = 'Nadralia#'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Password must have atleast 1 number between [0-9]")
    
    def test_special_character(self):
        password = 'Nadra2922'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Password must have atleast 1 character from [$#@]")

    def test_validate_user_details(self):
        """Tests to ensure the correct data definition passes"""
        username = "Adralia"
        email = "nadralia@gmail.com"
        gender = "Male"
        self.assertEqual(self.validation.validate_user_details(username,email,gender), 
         None)

    def test_validate_invalid_email(self):
        """Tests to ensure the correct data definition passes"""
        username = "Adralia"
        email = "nadraliagmail.com"
        gender = "Male"
        self.assertEqual(self.validation.validate_user_details(username,email,gender), 
         "Invalid email format")

    def test_validate_invalid_gender(self):
        """Tests to ensure the correct data definition passes"""
        username = "Adralia"
        email = "nadralia@gmail.com"
        gender = "ale"
        self.assertEqual(self.validation.validate_user_details(username,email,gender), 
         "Gender must be either Male or Female")

    def test_validate_login(self):
        """Tests to ensure the correct data definition passes"""
        username = "Adralia"
        password = ""
        self.assertEqual(self.validation.validate_login(username,password), 
         "Input username or password")

    def test_validate_missing_status(self):
        """Tests to ensure the correct data definition passes"""
        status = ""
        self.assertEqual(self.validation.validate_status(status), 
         "Status is missing")

    def test_validate_status(self):
        """Tests to ensure the correct data definition passes"""
        status = "drafted"
        self.assertEqual(self.validation.validate_status(status), 
         None)
    def test_validate_wrong_status(self):
        """Tests to ensure the correct data definition passes"""
        status = "housearrest"
        self.assertEqual(self.validation.validate_status(status), 
        "Status must be one of these drafted,resolved,under investigation,rejected")
    
