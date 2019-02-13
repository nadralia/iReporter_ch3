from api.models.incident import IncidentModel


class IncidentController:

    def __init__(self):
        """initialize objects and variables """
        self.incident_m = IncidentModel()
    
    def create_a_new_incident(self,incident_unique,createdBy, incident_type, status,latitude,longitude,
        images,videos,comment,createdOn):
        """create a new incident entry"""
        new_incident = IncidentModel(incident_unique=incident_unique,createdBy=createdBy,
                   incident_type=incident_type, status=status,
                   latitude=latitude, longitude=longitude, images=images,videos=videos,
                   comment=comment, createdOn=createdOn)

        self.incident_m.add_new_incident(incident_unique=new_incident.incident_unique,
                        createdBy=new_incident.createdBy,
                         incident_type=new_incident.incident_type, 
                         status=new_incident.status,latitude=new_incident.latitude, 
                         longitude=new_incident.longitude, images=new_incident.images,
                         videos=new_incident.videos,comment=new_incident.comment, 
                         createdOn=new_incident.createdOn)

        return True


    def does_incident_exist(self, incidentUnx,user_id):
        """check if incident exists."""
        incident_exists = self.incident_m.does_incident_exist(incidentUnx,user_id)
        if incident_exists:
            return incident_exists
        return False
        

    def fetch_all_incidents(self):
        """fetch all available incidents"""
        available_incidents = self.incident_m.get_all_incidents()
        return available_incidents 


    def fetch_all_incidents_by_user(self, user_id):
        """fetch all available incidents"""
        available_incidents = self.incident_m.get_all_incidents_by_user(user_id)
        return available_incidents 

    def get_all_incidents_by_type_of_user(self, user_id, incident_type):
        """fetch all available incidents by type"""
        available_incidents = self.incident_m.get_all_incidents_by_type_of_user(user_id,incident_type)
        return available_incidents 
        

    def get_single_incident(self, incident_id):
        """fetch a single incidents"""
        incident = self.incident_m.fetch_single_incident(incident_id=incident_id)
        if incident:
            return incident
        return False

    def get_single_incident_by_user(self, user_id ,incident_id):
        """fetch a single incident of a user """
        incident = self.incident_m.fetch_single_incident_of_user(user_id, incident_id)
        if incident:
            return incident
        return False

    def delete_incident(self, incident_id):
        """delete a incident"""
        delete_item = self.incident_m.delete_incident(incident_id=incident_id)
        if delete_item:
            return True
        return False
    
    def user_delete_incident(self, user_id, incident_id):
        """delete a incident"""
        delete_item = self.incident_m.delete_incident_of_user(user_id, incident_id)
        if delete_item:
            return True
        return False
    
    def update_incident(self, incident_type, status,latitude,longitude,
        images,videos,comment,incident_id):
        """update a incident"""
        update = self.incident_m.update_incident(incident_type=incident_type, 
                         status=status, latitude=latitude, 
                         longitude=longitude, images=images,
                         videos=videos, comment=comment, incident_id=incident_id)
        if update:
            return True
        else:
            return False
    
    def update_incident_by_user(self,user_id, incident_type,latitude,longitude,
        images,videos,comment,incident_id):
        """update a incident"""
        update = self.incident_m.update_incident_by_normal_user(createdBy=user_id,
                         incident_type=incident_type, 
                         latitude=latitude,longitude=longitude, images=images,
                         videos=videos,comment=comment,incident_id=incident_id)
        if update:
            return True
        else:
            return False

    def update_comment(self ,user_id,incident_id,comment):
        """update comment"""
        update = self.incident_m.update_comment(user_id,incident_id,comment)
        if update:
            return True
        else:
            return False
    
    def update_location(self ,user_id,incident_id,latitude,longitude):
        """update location"""
        update = self.incident_m.update_location(user_id,incident_id,latitude,longitude)
        if update:
            return True
        else:
            return False

    def update_status(self ,incident_id,status):
        """update status"""
        update = self.incident_m.update_status(incident_id,status)
        if update:
            return True
        else:
            return False
    
    def update_comment_admin(self ,incident_id,comment):
        """update comment"""
        update = self.incident_m.update_comment_admin(incident_id,comment)
        if update:
            return True
        else:
            return False
    
    def update_location_admin(self ,incident_id,latitude,longitude):
        """update location"""
        update = self.incident_m.update_location_admin(incident_id,latitude,longitude)
        if update:
            return True
        else:
            return False