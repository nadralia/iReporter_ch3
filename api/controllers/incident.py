from api.models.incident import IncidentModel
from api.database.db_functions import DBFunctions

class IncidentController:

    def __init__(self):
        """initialize objects and variables """
        self.dbfunctions = DBFunctions()
    
    def create_a_new_incident(self,createdBy, incident_type, status,latitude,longitude,
        images,videos,comment,createdOn):
        """create a new incident entry"""
        new_incident = IncidentModel(createdBy=createdBy,incident_type=incident_type, status=status,
                   latitude=latitude, longitude=longitude, images=images,videos=videos,
                   comment=comment, createdOn=createdOn)

        self.dbfunctions.add_new_incident(createdBy=new_incident.createdBy,
                         incident_type=new_incident.incident_type, 
                         status=new_incident.status,latitude=new_incident.latitude, 
                         longitude=new_incident.longitude, images=new_incident.images,
                         videos=new_incident.videos,comment=new_incident.comment, 
                         createdOn=new_incident.createdOn)

        return True

    def fetch_all_incidents(self):
        """fetch all available incidents"""
        available_incidents = self.dbfunctions.get_all_incidents()
        return available_incidents 


    def fetch_all_incidents_by_user(self, user_id):
        """fetch all available incidents"""
        available_incidents = self.dbfunctions.get_all_incidents_by_user(user_id)
        return available_incidents 

    def get_single_incident(self, incident_id):
        """fetch a single incidents"""
        incident = self.dbfunctions.fetch_single_incident(incident_id=incident_id)
        if incident:
            return incident
        return False

    def get_single_incident_by_user(self, user_id ,incident_id):
        """fetch a single incident of a user """
        incident = self.dbfunctions.fetch_single_incident_of_user(user_id, incident_id)
        if incident:
            return incident
        return False

    def delete_incident(self, incident_id):
        """delete a incident"""
        delete_item = self.dbfunctions.delete_incident(incident_id=incident_id)
        if delete_item:
            return True
        return False
    
    def user_delete_incident(self, user_id, incident_id):
        """delete a incident"""
        delete_item = self.dbfunctions.delete_incident_of_user(user_id, incident_id)
        if delete_item:
            return True
        return False
    
    def update_incident(self, incident_type, status,latitude,longitude,
        images,videos,comment,incident_id):
        """update a incident"""
        update = self.dbfunctions.update_incident(
                         incident_type=incident_type, 
                         status=status,latitude=latitude, 
                         longitude=longitude, images=images,
                         videos=videos,comment=comment,incident_id=incident_id)
        if update:
            return True
        else:
            return False
    
    def update_incident_by_user(self,user_id, incident_type,latitude,longitude,
        images,videos,comment,incident_id):
        """update a incident"""
        update = self.dbfunctions.update_incident_by_normal_user(createdBy=user_id,
                         incident_type=incident_type, 
                         latitude=latitude,longitude=longitude, images=images,
                         videos=videos,comment=comment,incident_id=incident_id)
        if update:
            return True
        else:
            return False

    
