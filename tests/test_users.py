from api.models.user import UserModel
from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json


class TestUsers(BaseTestCase):
    def setUp(self):
        kwargs = {
            "firstname": "Adralia",
            "lastname": "Nelson",
            "othernames": "Nelson",
            "email": "nadralia@gmail.com",
            "username": "nadralia",
            "password": "nadrA67#ad",
            "phonenumber": "+256770987654",
            "gender": "Male",
            "is_admin": "True"
        }
        self.user = UserModel(**kwargs)

    def test_class_instance(self):
        """Tests that the defined object is an instance of the User class"""
        self.assertIsInstance(self.user, UserModel)
    
    def test_check_username(self):
        pass


   