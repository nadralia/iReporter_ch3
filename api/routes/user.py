from flask import jsonify, request, Blueprint
from flask.views import MethodView
from datetime import datetime
from api.helpers.validations import Validation
from api.controllers.user import UserController
from api.database.db_functions import DBFunctions

validate = Validation()
user_controller = UserController()
user_blueprint = Blueprint("user_blueprint", __name__)


class RegisterUser(MethodView):
    def post(self):
        pass
       

registration_view = RegisterUser.as_view("registration_view")
user_blueprint.add_url_rule("/api/auth/register",view_func=registration_view, methods=["POST"])

class Login(MethodView):
    def post(self):
        pass
        

login_view = Login.as_view("login_view")
user_blueprint.add_url_rule("/api/auth/login",view_func=login_view, methods=["POST"])