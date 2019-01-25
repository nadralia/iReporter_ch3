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

                username =  get_current_user_identity()
                if username:
                    user = user_controller.get_user(username=username)
                    user_id = user["user_id"]
                    add_incident = incident_controller.create_a_new_incident(createdBy=user_id, 
                                incident_type=incident_type, status=status,latitude=latitude,
                                longitude=longitude,images=images, videos=videos, 
                                comment=comment ,createdOn=createdOn)
                    if add_incident:
                        return jsonify({
                            "message": "incident successfully added",
                            "incident":incident_controller.does_incident_exist(comment,user_id)
                            }), 201
                return jsonify({"message": "user identity unknown"}), 400

            return jsonify({"message": "Please use the corrects keys"}), 400
        except Exception as exception:
            return jsonify({"message": str(exception)}), 400
       


class FetchAllIncidents(MethodView):
    def get(self):
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



class FetchSingleIncident(MethodView):
    def get(self, incident_id):
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
                return jsonify({"incident_details": incident_details}), 200
            return jsonify({"message": "incident not added yet"}), 404

        

class DeleteIncident(MethodView):
    def delete(self, incident_id):
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
            else:
                return jsonify({"message": "incident not deleted, or doesn't exist"}), 400

        


class UpdateIncident(MethodView):
    def put(self, incident_id):
        is_admin = get_current_user_role()
        if is_admin == "True":
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
                username =  get_current_user_identity()
                user = user_controller.get_user(username=username)
                user_id = user["user_id"]

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
       
class EditComment(MethodView):
    def PATCH(self, incident_id):
        is_admin = get_current_user_role()
        if is_admin == "True":
            data = request.get_json()
            comment = data.get("comment") 
            updated_comment = incident_controller.update_comment_admin(incident_id,comment)
            if updated_comment:
                    return jsonify({
                        "message":
                            "incident comment successfully updated.",
                            "incident": incident_controller.get_single_incident(incident_id=incident_id)
                    }), 200
            return jsonify({"message": "incident not updated or doesn't exist"}), 400
        
        else:
            data = request.get_json()
            comment = data.get("comment") 
            username =  get_current_user_identity()
            user = user_controller.get_user(username=username)
            user_id = user["user_id"] 
            updated_comment = incident_controller.update_comment(user_id,incident_id,comment)
            if updated_comment:
                    return jsonify({
                        "message":
                            "incident comment successfully updated.",
                            "incident": incident_controller.get_single_incident_by_user(user_id ,incident_id)
                    }), 200
            return jsonify({"message": "incident not updated or doesn't exist"}), 400



class EditLocation(MethodView):
    def PATCH(self, incident_id):
        is_admin = get_current_user_role()
        if is_admin == "True":
            data = request.get_json()
            latitude = data.get("latitude") 
            longitude = data.get("longitude") 
            updated_location = incident_controller.update_location_admin(incident_id,latitude,longitude)
            if updated_location:
                    return jsonify({
                        "message":
                            "incident location successfully updated.",
                            "incident": incident_controller.get_single_incident(incident_id=incident_id)
                    }), 200
            return jsonify({"message": "incident not updated or doesn't exist"}), 400
        
        else:
            data = request.get_json()
            latitude = data.get("latitude") 
            longitude = data.get("longitude") 
            username =  get_current_user_identity()
            user = user_controller.get_user(username=username)
            user_id = user["user_id"] 
            updated_location = incident_controller.update_location(user_id,incident_id,latitude,longitude)
            if updated_location:
                    return jsonify({
                        "message":
                            "incident location successfully updated.",
                            "incident": incident_controller.get_single_incident_by_user(user_id ,incident_id)
                    }), 200
            return jsonify({"message": "incident not updated or doesn't exist"}), 400



class EditStatus(MethodView):
    def PATCH(self, incident_id):
        is_admin = get_current_user_role()
        if is_admin == "True":
            data = request.get_json()
            status = data.get("status") 
            updated_status = incident_controller.update_status(incident_id,status)
            if updated_status:
                    return jsonify({
                        "message":
                            "incident status successfully updated.",
                            "incident": incident_controller.get_single_incident(incident_id=incident_id)
                    }), 200
            return jsonify({"message": "incident not updated or doesn't exist"}), 400
        else:
            return jsonify({"message": "Only Admin can edit a status of incident"}), 400




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


edit_comment_view = EditComment.as_view("edit_comment_view")
incident_blueprint.add_url_rule(
    "/api/v2/incidents/<int:incident_id>/comment", view_func=edit_comment_view, methods=["PATCH"])

edit_location_view = EditLocation.as_view("edit_location_view")
incident_blueprint.add_url_rule(
    "/api/v2/incidents/<int:incident_id>/location", view_func=edit_location_view, methods=["PATCH"])


edit_status_view = EditStatus.as_view("edit_status_view")
incident_blueprint.add_url_rule(
    "/api/v2/incidents/<int:incident_id>/status", view_func=edit_status_view, methods=["PATCH"])