from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestDeletingIncidents(BaseTestCase):

    def test_deleting_incident_reporter(self):
        user_header= self.user_header()
        with self.app:
            response = self.add_incident()
            response2 = self.app.delete("/api/v2/incidents/1",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+user_header),)
            reply = json.loads(response2.data.decode())
            self.assertEqual(reply.get("message"), "incident successfully deleted")                
            self.assertEqual(response2.status_code, 200)

    
    def test_deleting_nonexistant_incident(self):
        user_header= self.user_header()
        response2 = self.app.delete("/api/v2/incidents/1",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+user_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "incident not deleted, or doesn't exist")                
        self.assertEqual(response2.status_code, 400)

    def test_deleting_incident_with_wrong_id(self):
        user_header= self.user_header()
        with self.app:
            response = self.add_incident()
            response2 = self.app.delete("/api/v2/incidents/e",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+user_header),)                 
            reply = json.loads(response2.data.decode())
            self.assertEqual(reply.get("message"), "Input should be an interger") 
            self.assertEqual(response2.status_code, 400) 

    def test_deleting_incident_admin(self):
        admin_header= self.admin_header()
        with self.app:
            response = self.add_incident_admin()
            response2 = self.app.delete("/api/v2/incidents/1",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+admin_header),)
            reply = json.loads(response2.data.decode())
            self.assertEqual(reply.get("message"), "incident successfully deleted")                
            self.assertEqual(response2.status_code, 200)

    
    def test_deleting_nonexistant_incident_admin(self):
        admin_header= self.admin_header()
        response2 = self.app.delete("/api/v2/incidents/1",
                                 content_type='application/json', 
                                 headers=dict(Authorization='Bearer '+admin_header),)
        reply = json.loads(response2.data.decode())
        self.assertEqual(reply.get("message"), "incident not deleted, or doesn't exist")                
        self.assertEqual(response2.status_code, 400)

    def test_deleting_incident_with_wrong_id_admin(self):
        admin_header= self.admin_header()
        with self.app:
            response = self.add_incident_admin()
            response2 = self.app.delete("/api/v2/incidents/e",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+admin_header),)                 
            reply = json.loads(response2.data.decode())
            self.assertEqual(reply.get("message"), "Input should be an interger") 
            self.assertEqual(response2.status_code, 400) 