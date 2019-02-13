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
more_incident_blueprint = Blueprint("more_incident_blueprint", __name__)

"""More Incident VIEWS"""

class EditComment(MethodView):
    def patch(self, incident_id):
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
            return jsonify({"message": updated_comment}), 400


edit_comment_view = EditComment.as_view("edit_comment_view")
more_incident_blueprint.add_url_rule(
    "/api/v2/incidents/<incident_id>/comment", view_func=edit_comment_view, methods=["PATCH"])


class EditLocation(MethodView):
    def patch(self, incident_id):
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


edit_location_view = EditLocation.as_view("edit_location_view")
more_incident_blueprint.add_url_rule(
    "/api/v2/incidents/<incident_id>/location", view_func=edit_location_view, methods=["PATCH"])



class EditStatus(MethodView):
    def patch(self, incident_id):
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

edit_status_view = EditStatus.as_view("edit_status_view")
more_incident_blueprint.add_url_rule(
    "/api/v2/incidents/<incident_id>/status", view_func=edit_status_view, methods=["PATCH"])


class GetAllRedflags(MethodView):
    def get(self):
        try:
            username =  get_current_user_identity()
            user = user_controller.get_user(username=username)
            user_id = user["user_id"]
            incident_type = "red-flag"
            all_redflags = incident_controller.get_all_incidents_by_type_of_user(user_id,incident_type)
            if all_redflags:
                return jsonify({"data": all_redflags}), 200
            return jsonify({"message": "no redlags added yet"}), 404

        except Exception as exception:
            return jsonify({"message": str(exception)}), 400

get_all_redflag_view = GetAllRedflags.as_view("get_all_redflag_view")
more_incident_blueprint.add_url_rule(
    "/api/v2/red-flags", view_func=get_all_redflag_view, methods=["GET"])

class GetAllInterventions(MethodView):
    def get(self):
        try:
            username =  get_current_user_identity()
            user = user_controller.get_user(username=username)
            user_id = user["user_id"]
            incident_type = "intervention"
            all_interventions = incident_controller.get_all_incidents_by_type_of_user(user_id,incident_type)
            if all_interventions:
                return jsonify({"data": all_interventions}), 200
            return jsonify({"message": "no interventions added yet"}), 404

        except Exception as exception:
            return jsonify({"message": str(exception)}), 400

get_all_intervention_view = GetAllInterventions.as_view("get_all_intervention_view")
more_incident_blueprint.add_url_rule(
    "/api/v2/interventions", view_func=get_all_intervention_view, methods=["GET"])