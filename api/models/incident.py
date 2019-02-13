from api.database.db_connection import DatabaseConnection

class IncidentModel:
    def __init__(self, **kwargs):
        """ stores incident details """
        self.incident_unique = kwargs.get('incident_unique')
        self.createdBy = kwargs.get('createdBy')
        self.incident_type = kwargs.get('incident_type')
        self.status = kwargs.get('status')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.images = kwargs.get('images')
        self.videos = kwargs.get('videos')
        self.comment = kwargs.get('comment')
        self.createdOn = kwargs.get('createdOn')
        self.connect = DatabaseConnection()
        self.cursor = self.connect.dict_cursor
    

    def add_new_incident(self,incident_unique,createdBy, incident_type, status,latitude,longitude,
        images,videos,comment,createdOn):
        """add new incident """
        query = (
            """INSERT INTO incidents (incident_unique,createdBy, incident_type, status, latitude, longitude, 
            images,videos,comment,createdOn) 
            VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}','{}','{}'
            )""".format(incident_unique,createdBy,incident_type,status,latitude, longitude,images,
            videos,comment,createdOn))

        self.cursor.execute(query)
    
    def does_incident_exist(self,incident_unique,user_id):
        """# check if comment exists."""
        query = ("""SELECT * FROM incidents where incident_unique = '{}' and createdBy = '{}'""".format(incident_unique,user_id))
        self.cursor.execute(query)
        incident = self.cursor.fetchone()
        if incident:
            return incident
        return False

    def get_all_incidents(self):
        """function to get all incidents"""
        self.cursor.execute("SELECT * from incidents")
        all_incidents = self.cursor.fetchall()
        return all_incidents

    def get_all_incidents_by_user(self, user_id):
        """function to get all incidents"""
        self.cursor.execute("SELECT * FROM incidents WHERE createdBy = '{}'" .format(user_id))
        all_incidents = self.cursor.fetchall()
        return all_incidents
        
    def get_all_incidents_by_type_of_user(self, user_id,incident_type):
        """function to get all incidents"""
        self.cursor.execute("SELECT * FROM incidents WHERE incident_type = '{}' and createdBy = '{}'" .format(incident_type,user_id))
        all_incidents = self.cursor.fetchall()
        return all_incidents

    def fetch_single_incident(self,incident_id):
        """function to get details of a incident"""
        self.cursor.execute("SELECT * FROM incidents WHERE incident_id = '{}'" .format(incident_id))
        row = self.cursor.fetchone()
        return row

    def fetch_single_incident_of_user(self,user_id, incident_id):
        """function a single incident """
        self.cursor.execute("""SELECT * from incidents where incident_id = '{}' and 
                             createdBy='{}'""".format(incident_id, user_id))
        row = self.cursor.fetchone()
        return row

    def delete_incident(self, incident_id):
        """function to delete a specific incident"""
        query = ("""DELETE FROM incidents WHERE incident_id = '{}'""" .format(incident_id))
        self.cursor.execute(query)
        delete = self.cursor.rowcount
        if int(delete) > 0:
            return True
        else:
            return False

    def delete_incident_of_user(self, user_id, incident_id):
        """function to delete a specific incident"""
        query = ("""DELETE FROM incidents WHERE incident_id = '{}' and 
                                createdBy='{}'""" .format(incident_id, user_id))
        self.cursor.execute(query)
        delete = self.cursor.rowcount
        if int(delete) > 0:
            return True
        else:
            return False

    def update_incident(self, incident_type, status,latitude,longitude,
        images,videos,comment,incident_id):
        """function to update incident"""
        try:
            query = ("""UPDATE incidents SET incident_type = '{}', status = '{}',
             latitude = '{}', longitude = '{}', images = '{}', videos = '{}',
              comment = '{}' where incident_id = '{}'
              """ .format(incident_type, status, latitude,longitude,images,videos,comment,incident_id))
            self.cursor.execute(query)
            count = self.cursor.rowcount
            if int(count) > 0:
                return True
            else:
                return False   
        except:
            return False
    
    def update_incident_by_normal_user(self, createdBy, incident_type,latitude,longitude,
        images,videos,comment,incident_id):
        """function to update incident"""
        try:
            query = ("""UPDATE incidents SET incident_type = '{}',
             latitude = '{}', longitude = '{}', images = '{}', videos = '{}',
              comment = '{}' where incident_id = '{}' and createdBy = '{}'
              """ .format(incident_type,latitude,longitude,images,videos,comment,incident_id,createdBy))
            self.cursor.execute(query)
            count = self.cursor.rowcount
            if int(count) > 0:
                return True
            else:
                return False   
        except:
            return False