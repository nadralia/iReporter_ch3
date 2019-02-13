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