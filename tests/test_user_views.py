from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestUserViews(BaseTestCase):

    def test_register(self):
        """Tests that the user is registered and logs in as reporter"""
        
        user_data = {
            "firstname": "Admin",
            "lastname": "ireporter",
            "othernames": "",
            "email": "adminireporter@gmail.com",
            "username": "admin007",
            "password": "nadra2526#A",
            "phonenumber": "+256779004531",
            "gender": "Male",
            "is_admin":"True"
        }
        response = self.app.post('api/v2/auth/signup',
                                    content_type='application/json',
                                    data=json.dumps(user_data))
        msg = json.loads(response.data)
        self.assertIn("User account created", msg['message'])
        self.assertEqual(response.status_code, 201)

    def test_user_not_registered(self):
        """Tests that the user is registered and logs in as reporter"""
        pass

    def test_registration_with_missing_keys(self):
        """ Test for missing keys """
        user_data = {
            "lastname": "ireporter",
            "othernames": "",
            "email": "adminireporter@gmail.com",
            "username": "admin007",
            "password": "nadra2526#A",
            "phonenumber": "+256779004531",
            "gender": "Male",
            "is_admin":"True"
        }
        response = self.app.post('api/v2/auth/signup',
                                    content_type='application/json',
                                    data=json.dumps(user_data))
        msg = json.loads(response.data)
        self.assertIn("Please provide the correct keys for the data", msg['message'])
        self.assertEqual(response.status_code, 400)

    def test_registration_with_wrong_username(self):
        """Test usename is missing"""
        user_data = {
            "firstname": "Admin",
            "lastname": "ireporter",
            "othernames": "",
            "email": "adminireporter@gmail.com",
            "username": "",
            "password": "nadra2526#A",
            "phonenumber": "+256779004531",
            "gender": "Male",
            "is_admin":"True"
        }
        response = self.app.post('api/v2/auth/signup',
                                    content_type='application/json',
                                    data=json.dumps(user_data))
        msg = json.loads(response.data)
        self.assertIn("usename is missing", msg['message'])
        self.assertEqual(response.status_code, 400)

    def test_registration_with_no_username(self):
        """ Test for successful user register """
        user_data = {
            "firstname": "Admin",
            "lastname": "ireporter",
            "othernames": "",
            "email": "adminireporter@gmail.com",
            "username": " ",
            "password": "nadra2526#A",
            "phonenumber": "+256779004531",
            "gender": "Male",
            "is_admin":"True"
        }
        response = self.app.post("api/v2/auth/signup",
                                 content_type='application/json',
                                 data=json.dumps(user_data)
                                 )                       
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "Only alphanumerics allowed in user name")
        self.assertEqual(response.status_code, 400)     
    
    def test_registration_with_existing_username(self):
        """ Test for successful user register """
        user_data = {
            "firstname": "Admin",
            "lastname": "ireporter",
            "othernames": "",
            "email": "adminireporter@gmail.com",
            "username": "admin007",
            "password": "nadra2526#A",
            "phonenumber": "+256779004531",
            "gender": "Male",
            "is_admin":"False"
        }
        response = self.app.post("api/v2/auth/signup",
                                 content_type='application/json',
                                 data=json.dumps(user_data)
                                 )
        response2 = self.app.post("api/v2/auth/signup",
                                 content_type='application/json',
                                 data=json.dumps(user_data)
                                 )                         
        reply = json.loads(response2.data)
        self.assertEqual(reply.get("message"), "username exists")
        self.assertEqual(response2.status_code, 409)

    def test_registration_with_no_password(self):
        """ Test for successful user register """
        user_data = {
            "firstname": "Admin",
            "lastname": "ireporter",
            "othernames": "",
            "email": "adminireporter@gmail.com",
            "username": "admin007",
            "password": "",
            "phonenumber": "+256779004531",
            "gender": "Male",
            "is_admin":"False"
        }
        response = self.app.post("api/v2/auth/signup",
                                 content_type='application/json',
                                 data=json.dumps(user_data)
                                 )
        reply = json.loads(response.data)
        self.assertEqual(reply.get("message"), "Minimum length of password: 6 and  Maximum length of password: 12")
        self.assertEqual(response.status_code, 400) 