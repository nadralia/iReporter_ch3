from flask import jsonify, request, Blueprint,make_response
from werkzeug.security import generate_password_hash, check_password_hash
from api.helpers.token import generate_token
from flask.views import MethodView
from datetime import datetime
from api.helpers.validations import Validation
from api.controllers.user import UserController

validate = Validation()
user_controller = UserController()
user_blueprint = Blueprint("user_blueprint", __name__)


class RegisterUser(MethodView):
    def post(self):
        data = request.get_json()
        search_keys = ("firstname", "lastname", "othernames" ,"email", "username", 
        "password", "phonenumber","gender","is_admin")
        if all(key in data.keys() for key in search_keys):
            firstname = data.get("firstname")
            lastname = data.get("lastname")
            othernames = data.get("othernames")
            email = data.get("email")
            username = data.get("username")
            password = data.get("password")
            phonenumber = data.get("phonenumber")
            gender = data.get("gender")
            is_admin = data.get("is_admin")
            hashed_password = generate_password_hash(password, method='sha256')

            #validate user details 
            invalid_password = validate.validate_password(password)
            invalid = validate.validate_user_details(username,email,gender)
            if invalid:
                return jsonify({"message": invalid}), 400
            if invalid_password != True :
                return jsonify({"message": invalid_password}), 400
            username_exists = user_controller.check_if_username_exists(username=username)
            if username_exists:
                return jsonify({"message": "username exists"}), 409
            
            new_user = user_controller.create_new_user(firstname=firstname, lastname=lastname,
                    othernames=othernames,email=email,username=username, password=hashed_password, 
                    phonenumber=phonenumber,gender=gender,is_admin=is_admin) 
            
            if new_user:
                user = user_controller.get_user(username=username)
                return jsonify({"message": "User account created","user":user}), 201
            else:
                return jsonify({"message": "User not created"}), 400

        return jsonify({"message": "Please provide the correct keys for the data"}), 400

            
       

registration_view = RegisterUser.as_view("registration_view")
user_blueprint.add_url_rule("/api/v2/auth/signup",view_func=registration_view, methods=["POST"])

class Login(MethodView):
    def post(self):
        data = request.get_json()
        search_keys = ("username", "password")
        if all(key in data.keys() for key in search_keys):
            username = data.get("username")
            password = data.get("password")
            invalid = validate.validate_login(username, password)
            if invalid:
                return jsonify({"message": invalid}), 400

            user = user_controller.check_if_username_exists(username=username)
            if user:
                if username == user["username"] and check_password_hash(user["password"], password):
                    response = (
                                jsonify(
                                    {
                                        "status": 200,
                                        "data": [
                                            {
                                                "token": generate_token(
                                                        user["username"], user["is_admin"]
                                                ),
                                                "message": "Logged in successfully",
                                            }
                                        ],
                                    }
                                ),
                                200,
                            )
                    return response
                return jsonify({"message": "Wrong password"}), 400
            return jsonify({"message": "wrong login credentials or user does not exist"}), 400
        return jsonify({"message": "Please provide the correct keys for the data"}), 400
        

login_view = Login.as_view("login_view")
user_blueprint.add_url_rule("/api/v2/auth/login",view_func=login_view, methods=["POST"])