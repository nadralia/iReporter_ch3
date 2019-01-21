import unittest
from api.helpers.validations import Validation
from api import app


class TestValidation(unittest.TestCase):
    """ Tests Reflag and user validations """

    def setUp(self):
        """Sets up the validation class """
        self.validation = Validation()

    def test_if_its_a_validate_password(self):
        password = 'Nadra2922@'
        result = self.validation.validate_password(password)
        self.assertEqual(result, "Valid Password")
 
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