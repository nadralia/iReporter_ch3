from api.models.user import UserModel
from tests.base_test import BaseTestCase
from flask import json


class TestUsers(BaseTestCase):
    def setUp(self):
        kwargs = {
            "firstname": "Adralia",
            "lastname": "Nelson",
            "email": "nadralia@gmail.com",
            "username": "nadralia",
            "password": "nadrA67#ad",
            "phonenumber": "+256770987654",
            "gender": "Male",
            "registered": "2018-12-20 10:02:49",
            "is_admin": True
        }
        self.user = UserModel(**kwargs)