from api.models.incident import IncidentModel
from tests.base_test import BaseTestCase
from run import app
from flask import jsonify, json

class TestIncidents(BaseTestCase):
    def setUp(self):
        kwargs = {
            "createdBy": 1,
            "incident_type": "Nelson",
            "status": "Nelson",
            "latitude": "6.5951139",
            "longitude": "3.3429975",
            "images": "extortion.jpg",
            "videos": "extortion.mp4",
            "comment": "Extortion at the URA",
            "createdOn": "2018-12-20 10:02:49"
        }
        self.incident = IncidentModel(**kwargs)
    
    def test_delete_incident(self):
        pass
    
    def test_delete_incident_of_user(self):
        pass
    
    def test_update_incident(self):
        pass

    def test_update_incident_by_normal_user(self):
        pass