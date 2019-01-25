from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestDeletingIncidents(BaseTestCase):

    def test_deleting_incident_reporter(self):
        user_header= self.user_header()
        incident_data = {
            "incident_type": "red-flag",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
        }
        response = self.app.post("/api/v2/incidents",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+user_header),
                                 data=json.dumps(incident_data)   
                             )
        response2 = self.app.delete("/api/v2/incidents/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+user_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "incident successfully deleted")                
        self.assertEqual(response2.status_code, 200)

    
    def test_deleting_nonexistant_incident(self):
        user_header= self.user_header()
        response2 = self.app.delete("/api/v2/incidents/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+user_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "incident not deleted, or doesn't exist")                
        self.assertEqual(response2.status_code, 400)

    def test_deleting_incident_with_wrong_id(self):
        user_header= self.user_header()
        incident_data = {
            "incident_type": "red-flag",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
        }
        response = self.app.post("/api/v2/incidents",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+user_header),
                                 data=json.dumps(incident_data)   
                             )
        response2 = self.app.delete("/api/v2/incidents/e",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+user_header),)                 
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "Input should be an interger") 
        self.assertEqual(response2.status_code, 400) 

    def test_deleting_incident_admin(self):
        admin_header= self.admin_header()
        incident_data = {
            "incident_type": "red-flag",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
        }
        response = self.app.post("/api/v2/incidents",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),
                                 data=json.dumps(incident_data)   
                             )
        response2 = self.app.delete("/api/v2/incidents/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "incident successfully deleted")                
        self.assertEqual(response2.status_code, 200)

    
    def test_deleting_nonexistant_incident_admin(self):
        admin_header= self.admin_header()
        response2 = self.app.delete("/api/v2/incidents/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "incident not deleted, or doesn't exist")                
        self.assertEqual(response2.status_code, 400)

    def test_deleting_incident_with_wrong_id_admin(self):
        admin_header= self.admin_header()
        incident_data = {
            "incident_type": "red-flag",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
        }
        response = self.app.post("/api/v2/incidents",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),
                                 data=json.dumps(incident_data)   
                             )
        response2 = self.app.delete("/api/v2/incidents/e",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),)                 
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "Input should be an interger") 
        self.assertEqual(response2.status_code, 400) 