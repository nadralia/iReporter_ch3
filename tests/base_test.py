import unittest
from run import app
from flask import json
from api.database.db_connection import DatabaseConnection
from api.controllers.user import UserController
from api.helpers.token import generate_token

db_conn = DatabaseConnection()
user_controller = UserController()

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.firstname = "firstname"
        self.lastname = "lastname"
        self.othernames = "othernames"
        self.email = "admin@gmail.com"
        self.username = "admin123"
        self.password = "admin123N#"
        self.phonenumber = "0779-003100"
        self.gender = "Male"
        self.is_admin = "True"
        self.app = app.test_client(self)
        db_conn.create_tables()
        
    
    def tearDown(self):
        """Method to drop tables after the test is run"""
        db_conn.delete_tables()

    
    def admin_header(self):
        pass

    def user_header(self):
        pass