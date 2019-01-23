
class IncidentModel:
    def __init__(self, **kwargs):
        """ stores incident details """
        self.createdBy = kwargs.get('createdBy')
        self.incident_type = kwargs.get('incident_type')
        self.status = kwargs.get('status')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.images = kwargs.get('images')
        self.videos = kwargs.get('videos')
        self.comment = kwargs.get('comment')
        self.createdOn = kwargs.get('createdOn')