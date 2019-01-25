from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestViewingIncidents(BaseTestCase):

    def test_viewing_nonexistant_incidents(self):
        admin_header= self.admin_header()
        response2 = self.app.get("/api/v2/incidents",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "no incidents added yet")                
        self.assertEqual(response2.status_code, 404)

    def test_viewing_nonexistant_incident(self):
        """admin_header= self.admin_header()
        response2 = self.app.get("/api/v2/incidents/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "incident not added yet")                
        self.assertEqual(response2.status_code, 404)""" 
        pass
    
    def test_viewing_available_products(self):
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
        response2 = self.app.get("/api/v2/incidents",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),)                 
        self.assertEqual(response2.status_code, 200)

    def test_viewing_single_incident(self):
        """admin_header= self.admin_header()
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
        response2 = self.app.get("/api/v2/incidents/1",
                                 content_type='application/json', headers=dict(Authorization='Bearer '+admin_header),)                 
        self.assertEqual(response2.status_code, 200)"""

    