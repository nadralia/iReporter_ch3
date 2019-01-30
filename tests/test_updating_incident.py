from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestUpdatingIncidents(BaseTestCase):
    
    def test_updating_nonexistant_incident(self):
        user_header= self.user_header()
        _data = {
            "incident_type": "intervention",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
            }
        with self.app:
            response = self.add_incident()
            response1 = self.app.put("/api/v2/incidents/2",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+user_header),
                                    data=json.dumps(_data)   
                                )                      
            reply = json.loads(response1.data.decode())
            self.assertEqual(reply.get("message"), "incident not updated or doesn't exist")
            self.assertEqual(response1.status_code, 400)

    def test_updating_incident(self):
        user_header= self.user_header()
        _data = {
            "incident_type": "intervention",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
            }
        with self.app:
            response = self.add_incident()
            response = self.app.put("/api/v2/incidents/1",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+user_header),
                                    data=json.dumps(_data)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "incident successfully updated.")
            self.assertEqual(response.status_code, 200)

    def test_updating_incident_impromper_id(self):
        user_header= self.user_header()
        _data = {
            "incident_type": "intervention",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
            }
        with self.app:
            response = self.add_incident()
            response = self.app.put("/api/v2/incidents/a",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+user_header),
                                    data=json.dumps(_data)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "Input should be an interger")
            self.assertEqual(response.status_code, 400)

    def test_updating_incident_wrong_incident_id(self):
        pass

    def test_updating_incident_missing_keys(self):
        admin_header= self.admin_header()
        _data = {
            "incident_type": "intervention",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the FDC"
            }
        with self.app:
            response = self.add_incident_admin()
            response = self.app.put("/api/v2/incidents/1",
                                    content_type='application/json', 
                                    headers=dict(Authorization='Bearer '+admin_header),
                                    data=json.dumps(_data)   
                                )                      
            reply = json.loads(response.data.decode())
            self.assertEqual(reply.get("message"), "Please use the corrects keys")
            self.assertEqual(response.status_code, 400)                                