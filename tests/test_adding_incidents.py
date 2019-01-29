from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestIncidents(BaseTestCase):

    def test_adding_incident_successfully(self):
        with self.app:
            response = self.add_incident()
            reply = json.loads(response.data.decode())
            self.assertIn("incident successfully added", reply['message'])
            self.assertEqual(response.status_code, 201)

    def test_adding_incident_no_comments(self):
        admin_header= self.admin_header()
        incident_data = {
            "incident_type": "red-flag",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": ""
        }
        response = self.app.post("/api/v2/incidents",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin_header),
                                 data=json.dumps(incident_data)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "Comment of the incident is missing")
        self.assertEqual(response.status_code, 400)

    def test_adding_incident_no_type(self):
        admin_header= self.admin_header()
        incident_data = {
            "incident_type": "",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
        }
        response = self.app.post("/api/v2/incidents",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin_header),
                                 data=json.dumps(incident_data)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "Type of incident is missing")
        self.assertEqual(response.status_code, 400)

    def test_adding_incident_wrong_type(self):
        admin_header= self.admin_header()
        incident_data = {
            "incident_type": "buton",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
        }
        response = self.app.post("/api/v2/incidents",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin_header),
                                 data=json.dumps(incident_data)   
                             )          
        reply = json.loads(response.data.decode())
        self.assertEqual(reply.get("message"), "Type of incident must be either Red-flag or Intervention")
        self.assertEqual(response.status_code, 400)