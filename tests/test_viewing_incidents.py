from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestViewingIncidents(BaseTestCase):

    def test_viewing_nonexistant_incidents(self):
        admin_header= self.admin_header()
        response2 = self.app.get("/api/v2/incidents",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "no incidents added yet")                
        self.assertEqual(response2.status_code, 404)

    def test_viewing_nonexistant_incident(self):
        admin_header= self.admin_header()
        response2 = self.app.get("/api/v2/incidents/1",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "incident not added yet")                
        self.assertEqual(response2.status_code, 404)
    
    def test_viewing_available_products(self):
        admin_header= self.admin_header()
        with self.app:
            response = self.add_incident_admin()
            response2 = self.app.get("/api/v2/incidents",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+admin_header),)                 
            self.assertEqual(response2.status_code, 200)

    def test_viewing_single_incident(self):
        admin_header= self.admin_header()
        with self.app:
            response = self.add_incident_admin()
            response2 = self.app.get("/api/v2/incidents/1",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+admin_header),)                 
            self.assertEqual(response2.status_code, 200)

    