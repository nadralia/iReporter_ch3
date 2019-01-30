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
        self.firstname = "Admin"
        self.lastname = "iReporter"
        self.othernames = "othernames"
        self.email = "admin@gmail.com"
        self.username = "admin123"
        self.password = "admin123N#"
        self.phonenumber = "0779-003100"
        self.gender = "Male"
        self.is_admin = "True"
        self.app = app.test_client(self)
        db_conn.create_tables()
        self.register_admin()
        self.register_reporter()
        
    
    def tearDown(self):
        """Method to drop tables after the test is run"""
        db_conn.delete_tables()

    def register_admin(self):
        user_controller.create_new_user(self.firstname,self.lastname,
        self.othernames,self.email,self.username, self.password, 
        self.phonenumber,self.gender,self.is_admin)
        
    def register_reporter(self):
        user_controller.create_new_user("adralia","nelson","mandela","nadralia@gmail.com", 
                         "nadralia","nadra29#liA","0703-000001",
                                  "Male", "False")

    def admin_header(self):
       token = generate_token(self.username, self.is_admin)
       return token


    def user_header(self):
       token = generate_token("nadralia", "False")
       return token
    
    def add_incident(self):
        """
        Function to create a incident
        """
        user_header= self.user_header()
        incident_data = {
            "incident_type": "red-flag",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
        }
        return self.app.post("/api/v2/incidents",
                        content_type='application/json',
                        headers=dict(Authorization='Bearer '+user_header),
                        data=json.dumps(incident_data)   
                    ) 
    def add_incident_admin(self):
        """
        Function to create a incident
        """
        admin_header= self.admin_header()
        incident = {
            "incident_type": "intervention",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extort.jpg",
            "videos": "extort.mp4",
            "comment": "Extortion at the URA"
        }
        return self.app.post("/api/v2/incidents",
                        content_type='application/json',
                        headers=dict(Authorization='Bearer '+admin_header),
                        data=json.dumps(incident)   
                    ) 