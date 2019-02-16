from flask import jsonify, request, Blueprint
import os
import uuid
from flask.views import MethodView
from datetime import datetime
from flasgger.utils import swag_from
from api.helpers.validations import Validation
from api.controllers.incident import IncidentController
from api.controllers.user import UserController
from api.helpers.token import (get_current_user_identity,
                                get_current_user_role)

validate = Validation()
incident_controller = IncidentController()
user_controller = UserController()
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
                incidentUnx = uuid.uuid4()
                invalid = validate.validate_incident(
                    incident_type,comment)
                if invalid:
                    return jsonify({"message": invalid}), 400
                validate_location = validate.validate_location(
                    latitude,longitude)
                if invalid:
                    return jsonify({"message": invalid}), 400

                username =  get_current_user_identity()
                if username:
                    user = user_controller.get_user(username=username)
                    user_id = user["user_id"]
                    add_incident = incident_controller.create_a_new_incident(incident_unique=incidentUnx,createdBy=user_id, 
                                incident_type=incident_type, status=status,latitude=latitude,
                                longitude=longitude,images=images, videos=videos, 
                                comment=comment ,createdOn=createdOn)
                    if add_incident:
                        return jsonify({
                            "message": "incident successfully added",
                            "incident":incident_controller.does_incident_exist(incidentUnx,user_id)
                            }), 201
                return jsonify({"message": "user identity unknown"}), 400

            return jsonify({"message": "Please use the corrects keys"}), 400
        except Exception as exception:
            return jsonify({"message": str(exception)}), 400

class UploadFiles(MethodView):
    def post(self):
        if request.method == 'POST':
            APP_ROOT = os.path.dirname(os.path.abspath(__file__))
            target = os.path.join(APP_ROOT, 'uploads/')
            if not os.path.isdir(target):
                os.mkdir(target)

            for file in request.files.getlist("file"):
                filename = file.filename
                destination = "/".join([target, filename])
                file.save(destination)
            return jsonify({"message": "file uploaded successfully"}), 200

       
class FetchAllIncidents(MethodView):
    def get(self):
        try:
            is_admin = get_current_user_role()
            if is_admin == "True":
                all_incidents = incident_controller.fetch_all_incidents()
                if all_incidents:
                    return jsonify({"available_incidents": all_incidents}), 200
                return jsonify({"message": "no incidents added yet"}), 404
            else:
                username =  get_current_user_identity()
                user = user_controller.get_user(username=username)
                user_id = user["user_id"]
                all_incidents = incident_controller.fetch_all_incidents_by_user(user_id)
                if all_incidents:
                    return jsonify({"available_incidents": all_incidents}), 200
                return jsonify({"message": "no incidents added yet"}), 404

        except Exception as exception:
            return jsonify({"message": str(exception)}), 400
class FetchSingleIncident(MethodView):
    def get(self, incident_id):
        try:
            is_admin = get_current_user_role()
            if is_admin == "True":
                invalid = validate.validate_input_type(incident_id)
                if invalid:
                    return jsonify({"message": invalid}), 400
                incident_details = incident_controller.get_single_incident(
                    incident_id=incident_id)
                if incident_details:
                    return jsonify({"incident_details": incident_details}), 200
                return jsonify({"message": "incident not added yet"}), 404
            else:
                username =  get_current_user_identity()
                user = user_controller.get_user(username=username)
                user_id = user["user_id"]
                invalid = validate.validate_input_type(incident_id)
                if invalid:
                    return jsonify({"message": invalid}), 400
                incident_details = incident_controller.get_single_incident_by_user(user_id,
                    incident_id)
                if incident_details:
                    if incident_details['deleted'] == "False":
                        return jsonify({"incident_details": incident_details}), 200
                    return jsonify({"message": "incident was deleted"}), 404
                return jsonify({"message": "incident not added yet"}), 404
        except Exception as exception:
            return jsonify({"message": str(exception)}), 400

class DeleteIncident(MethodView):
    def delete(self, incident_id):
        try:
            is_admin = get_current_user_role()
            if is_admin == "True":
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
                username =  get_current_user_identity()
                user = user_controller.get_user(username=username)
                user_id = user["user_id"]
                delete = incident_controller.user_delete_incident(user_id,incident_id)
                if delete:
                    return jsonify({"message": "incident successfully deleted"}), 200
                return jsonify({"message": "incident not deleted, or doesn't exist"}), 400
        except Exception as exception:
            return jsonify({"message": str(exception)}), 400


add_incident_view = AddIncident.as_view("add_incident_view")
upload_file_view = UploadFiles.as_view("upload_file_view")
fetch_all_incidents_view = FetchAllIncidents.as_view("fetch_all_incidents_view")
fetch_single_incident_view = FetchSingleIncident.as_view("fetch_single_incident_view")
delete_incident_view = DeleteIncident.as_view("delete_incident_view")

incident_blueprint.add_url_rule(
    "/api/v2/incidents", view_func=add_incident_view, methods=["POST"])
incident_blueprint.add_url_rule(
    "/api/v2/uploads", view_func=upload_file_view, methods=["POST"])
incident_blueprint.add_url_rule(
    "/api/v2/incidents", view_func=fetch_all_incidents_view, methods=["GET"])
incident_blueprint.add_url_rule("/api/v2/incidents/<incident_id>",
                             view_func=fetch_single_incident_view, methods=["GET"])
incident_blueprint.add_url_rule(
    "/api/v2/incidents/<incident_id>", view_func=delete_incident_view, methods=["DELETE"])
