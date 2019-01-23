from flask import jsonify, request, Blueprint
from flask.views import MethodView
from datetime import datetime
from api.helpers.validations import Validation
from api.controllers.incident import IncidentController
from api.controllers.user import UserController
from api.database.db_functions import DBFunctions
from api.helpers.token import (get_current_user_identity,
                                get_current_user_role)

validate = Validation()
incident_controller = IncidentController()
user_controller = UserController()

db_func = DBFunctions()
incident_blueprint = Blueprint("incident_blueprint", __name__)

"""Incident VIEWS"""
class AddIncident(MethodView):
    def post(self):
        try:
            data = request.get_json()
            search_keys = ("incident_type", "latitude","longitude","images","videos","comment")
            if all(key in data.keys() for key in search_keys):
                images = data.get("images")
                videos = data.get("videos")
                comment = data.get("comment")
                latitude = data.get("latitude")
                incident_type = data.get("incident_type")
                longitude = data.get("longitude")
                status = "drafted"
                createdOn = datetime.now()
            
                invalid = validate.validate_incident(
                    incident_type,comment)
                if invalid:
                    return jsonify({"message": invalid}), 400
                validate_location = validate.validate_location(
                    latitude,longitude)
                if invalid:
                    return jsonify({"message": invalid}), 400

                user_id =  get_current_user_identity()
                if user_id:
                    add_incident = incident_controller.create_a_new_incident(createdBy=user_id, 
                                incident_type=incident_type, status=status,latitude=latitude,
                                longitude=longitude,images=images, videos=videos, 
                                comment=comment ,createdOn=createdOn)
                    if add_incident:
                        return jsonify({"message": user_id}), 201
                return jsonify({"message": "user identity unknown"}), 400

            return jsonify({"message": "Please use the corrects keys"}), 400
        except Exception as exception:
            return jsonify({"message": str(exception)}), 400
       


class FetchAllIncidents(MethodView):
    def get(self):
        is_admin = get_current_user_role()
        if is_admin == True:
            all_incidents = incident_controller.fetch_all_incidents()
            if all_incidents:
                return jsonify({"available_incidents": all_incidents}), 200
            return jsonify({"message": "no incidents added yet"}), 404
        else:
            get_user = get_current_user_identity() 
            all_incidents = incident_controller.fetch_all_incidents_by_user(get_user)
            if all_incidents:
                return jsonify({"available_incidents": all_incidents}), 200
            return jsonify({"message": "no incidents added yet"}), 404



class FetchSingleIncident(MethodView):
    def get(self, incident_id):
        is_admin = get_current_user_role()
        if is_admin == True:
            invalid = validate.validate_input_type(incident_id)
            if invalid:
                return jsonify({"message": invalid}), 400
            incident_details = incident_controller.get_single_incident(
                incident_id=incident_id)
            if incident_details:
                return jsonify({"incident_details": incident_details}), 200
            return jsonify({"message": "incident not added yet"}), 404
        else:
            get_user = get_current_user_identity()
            invalid = validate.validate_input_type(incident_id)
            if invalid:
                return jsonify({"message": invalid}), 400
            incident_details = incident_controller.get_single_incident_by_user(get_user,
                incident_id)
                
            if incident_details:
                return jsonify({"incident_details": incident_details}), 200
            return jsonify({"message": "incident not added yet"}), 404

        

class DeleteIncident(MethodView):
    def delete(self, incident_id):
        is_admin = get_current_user_role()
        if is_admin == True:
            invalid = validate.validate_input_type(incident_id)
            if invalid:
                return jsonify({"message": invalid}), 400
            delete = incident_controller.delete_incident(incident_id=incident_id)
            if delete:
                return jsonify({"message": "incident successfully deleted"}), 200
            else:
                return jsonify({"message": "incident not deleted, or doesn't exist"}), 400
        
        else:
            invalid = validate.validate_input_type(incident_id)
            if invalid:
                return jsonify({"message": invalid}), 400
            user_id = get_current_user_identity()
            delete = incident_controller.user_delete_incident(user_id,incident_id)
            if delete:
                return jsonify({"message": "incident successfully deleted"}), 200
            else:
                return jsonify({"message": "incident not deleted, or doesn't exist"}), 400

        


class UpdateIncident(MethodView):
    def put(self, incident_id):
        is_admin = get_current_user_role()
        if is_admin == True:
            invalid_id = validate.validate_input_type(incident_id)
            if invalid_id:
                return jsonify({"message": invalid_id}), 400
            data = request.get_json()
            search_keys = ("incident_type", "status", "latitude","longitude","images","videos","comment")
            if all(key in data.keys() for key in search_keys):
                images = data.get("images")
                videos = data.get("videos")
                comment = data.get("comment")
                latitude = data.get("latitude")
                incident_type = data.get("incident_type")
                longitude = data.get("longitude")
                status = data.get("status")

                update = incident_controller.update_incident(incident_type=incident_type, 
                                status=status,latitude=latitude,
                                longitude=longitude,images=images, videos=videos, 
                                comment=comment,incident_id=incident_id)
                if update:
                    return jsonify({
                        "message":
                            "incident successfully updated.",
                            "incident": incident_controller.get_single_incident(incident_id=incident_id)
                    }), 200
                return jsonify({"message": "incident not updated or doesn't exist"}), 400
            return jsonify({"message": "Please use the corrects keys"}), 400
        else:
            invalid_id = validate.validate_input_type(incident_id)
            if invalid_id:
                return jsonify({"message": invalid_id}), 400
            data = request.get_json()
            search_keys = ("incident_type", "latitude","longitude","images","videos","comment")
            if all(key in data.keys() for key in search_keys):
                images = data.get("images")
                videos = data.get("videos")
                comment = data.get("comment")
                latitude = data.get("latitude")
                incident_type = data.get("incident_type")
                longitude = data.get("longitude")
                user_id = get_current_user_identity()

                update = incident_controller.update_incident_by_user(user_id=user_id,incident_type=incident_type, 
                                latitude=latitude,longitude=longitude,images=images, videos=videos, 
                                comment=comment,incident_id=incident_id)
                if update:
                    return jsonify({
                        "message":
                            "incident successfully updated.",
                            "incident": incident_controller.get_single_incident_by_user(user_id ,incident_id)
                    }), 200
                return jsonify({"message": "incident not updated or doesn't exist"}), 400

            return jsonify({"message": "Please use the corrects keys"}), 400
       


add_incident_view = AddIncident.as_view("add_incident_view")
fetch_all_incidents_view = FetchAllIncidents.as_view("fetch_all_incidents_view")
fetch_single_incident_view = FetchSingleIncident.as_view("fetch_single_incident_view")
delete_incident_view = DeleteIncident.as_view("delete_incident_view")
update_incident_view = UpdateIncident.as_view("update_incident_view")

incident_blueprint.add_url_rule(
    "/api/v2/incidents", view_func=add_incident_view, methods=["POST"])
incident_blueprint.add_url_rule(
    "/api/v2/incidents", view_func=fetch_all_incidents_view, methods=["GET"])
incident_blueprint.add_url_rule("/api/v2/incidents/<incident_id>",
                             view_func=fetch_single_incident_view, methods=["GET"])
incident_blueprint.add_url_rule(
    "/api/v2/incidents/<incident_id>", view_func=delete_incident_view, methods=["DELETE"])
incident_blueprint.add_url_rule(
    "/api/v2/incidents/<incident_id>", view_func=update_incident_view, methods=["PUT"])